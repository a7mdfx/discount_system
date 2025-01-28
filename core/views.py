from django.shortcuts import render
from rest_framework import generics
from .models import UserProfile, Order
from .serializers import UserProfileSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from rest_framework.views import APIView
from django.db.models import Q
from .models import Log
from .serializers import LogSerializer

# View to get user profile details
class UserProfileDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@api_view(['GET'])
def get_user_profile(request, user_id):
    try:
        user_profile_object = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        return Response(
            data={
                "message": "User not found"
            },
            status=404
        )

    serializer = UserProfileSerializer(instance=user_profile_object)
    user_profile_data = serializer.data

    return Response(
        data=user_profile_data,
        status=200
    )

@api_view(['GET'])
def get_user_list(request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data, status=200)


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()  # Get all orders
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    def get(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response({'message': 'Order deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    

class UserOrdersHistoryView(APIView):
    def get(self, request, user_id):
        # Step 1: Get the query parameters
        page = request.query_params.get('page', 1)  # Default to page 1
        limit = request.query_params.get('limit', 10)  # Default limit is 10 items per page

        # Step 2: Filter orders by user_id
        user_orders = Order.objects.filter(user_id=user_id).order_by('-created_at')

        # Step 3: Paginate the results
        paginator = Paginator(user_orders, limit)
        orders_page = paginator.get_page(page)

        # Step 4: Serialize the data
        serializer = OrderSerializer(orders_page, many=True)

        # Step 5: Prepare the response
        response_data = {
            "orders": serializer.data,
            "total": paginator.count,  # Total number of orders
            "page": orders_page.number,  # Current page number
        }
        return Response(response_data, status=200)
    

# View to calculate discounts
#@api_view(['POST'])
#def calculate_discount(request):
 #   user_id = request.data.get('user_id')
  #  items = request.data.get('items')
    
    # Add logic here to calculate discounts based on the rules.
    # Calculate the subtotal, discount amount, and final amount.

    # Example response:
   # return Response({
    #    'subtotal': 100.0,
     #   'discounts': [
      #      {'type': 'Loyalty', 'amount': 10.0},
       #     {'type': 'Cart', 'amount': 15.0}
        #],
        #'total_discount': 25.0,
        #'final_amount': 75.0
    #})

class CalculateDiscountView(APIView):
    def post(self, request):
        # Step 1: Extract data from the request
        data = request.data
        user_id = data.get('user_id')
        items = data.get('items', [])
        
        # Step 2: Initialize variables
        subtotal = 0
        discounts = []
        total_discount = 0
        final_amount = 0

        # Step 3: Calculate the subtotal
        for item in items:
            quantity = item.get('quantity', 0)
            price = item.get('price', 0)
            subtotal += quantity * price

        # Step 4: Apply discounts (example logic)
        # Example 1: 10% discount if subtotal > 100
        if subtotal > 100:
            discount_amount = subtotal * 0.1
            discounts.append({
                "type": "10% Discount for orders over $100",
                "amount": round(discount_amount, 2)
            })
            total_discount += discount_amount

        # Example 2: $5 discount for each item in the cart
        item_discount = len(items) * 5
        discounts.append({
            "type": "$5 discount per item",
            "amount": round(item_discount, 2)
        })
        total_discount += item_discount

        # Step 5: Calculate the final amount
        final_amount = subtotal - total_discount

        # Step 6: Return the response
        response_data = {
            "subtotal": round(subtotal, 2),
            "discounts": discounts,
            "total_discount": round(total_discount, 2),
            "final_amount": round(final_amount, 2)
        }
        return Response(response_data, status=200)


class LogListView(APIView):
    def get(self, request):
        # Query Parameters
        user_id = request.query_params.get('user_id', None)
        action_type = request.query_params.get('action_type', None)
        from_date = request.query_params.get('from_date', None)
        to_date = request.query_params.get('to_date', None)

        # Base QuerySet
        logs = Log.objects.all()

        # Filtering
        if user_id:
            logs = logs.filter(user_id=user_id)
        if action_type:
            logs = logs.filter(action_type=action_type)
        if from_date and to_date:
            logs = logs.filter(created_at__range=[from_date, to_date])

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = request.query_params.get('limit', 10)  # Default limit to 10
        result_page = paginator.paginate_queryset(logs, request)

        # Serialize Data
        serializer = LogSerializer(result_page, many=True)

        # Response
        return paginator.get_paginated_response(serializer.data)
    


def create_log(user_id, action_type, details):
    Log.objects.create(
        user_id=user_id,
        action_type=action_type,
        details=details
    )
