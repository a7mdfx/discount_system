from rest_framework import serializers
from .models import Discount


class CalculateDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'rule_name', 'min_order_amount', 'percentage', 'max_discount_amount']
