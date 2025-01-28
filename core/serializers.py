# core/serializers.py
from rest_framework import serializers
from .models import UserProfile, Order, OrderItem,Discount
from .models import Log


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'created_at', 'orders_count', 'total_spent', 'loyalty_status']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product_text', 'quantity', 'price']
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # Serialize related OrderItems

    class Meta:
        model = Order
        fields = ['id', 'user', 'subtotal', 'discount_amount', 'final_amount', 'status', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')  # Extract items data
        order = Order.objects.create(**validated_data)  # Create order
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)  # Create related order items
        return order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'subtotal', 'discount_amount', 'final_amount']  # Include the fields you need

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'rule_name', 'min_order_amount', 'percentage', 'max_discount_amount']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['log_id', 'user_id', 'action_type', 'details', 'created_at']