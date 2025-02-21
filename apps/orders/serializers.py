from rest_framework import serializers
from .models import Order, OrderItem


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