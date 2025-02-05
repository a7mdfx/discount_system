from django.shortcuts import render
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

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

