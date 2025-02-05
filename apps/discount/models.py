from django.db import models

  
# Discount Model (Optional: If you want to store discount rules)
class Discount(models.Model):
    rule_name = models.CharField(max_length=100)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.rule_name