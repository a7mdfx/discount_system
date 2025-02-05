from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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


