from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from apps.discount.serializers import CalculateDiscountSerializer



class CalculateDiscountView(generics.CreateAPIView):
    serializer_class = CalculateDiscountSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user_id = data.get('user_id')
        items = data.get('items', [])
        
        # Initialize variables
        subtotal = sum(item.get('quantity', 0) * item.get('price', 0) for item in items)
        discounts = []
        total_discount = 0

        # Apply discounts
        if subtotal > 100:
            discount_amount = subtotal * 0.1
            discounts.append({"type": "10% Discount for orders over $100", "amount": round(discount_amount, 2)})
            total_discount += discount_amount

        item_discount = len(items) * 5
        discounts.append({"type": "$5 discount per item", "amount": round(item_discount, 2)})
        total_discount += item_discount

        # Calculate final amount
        final_amount = subtotal - total_discount

        response_data = {
            "subtotal": round(subtotal, 2),
            "discounts": discounts,
            "total_discount": round(total_discount, 2),
            "final_amount": round(final_amount, 2)
        }

        return Response(response_data, status=200)


