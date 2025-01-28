from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# User Model
class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    orders_count = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    loyalty_status = models.CharField(max_length=20, default="Basic")

    def __str__(self):
        return self.email


# Order Model
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="orders")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.user.email}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Link to the order
    product_text = models.CharField(max_length=255)  # Product name
    quantity = models.IntegerField()  # Quantity of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per item
    
# Discount Model (Optional: If you want to store discount rules)
class Discount(models.Model):
    rule_name = models.CharField(max_length=100)
    min_order_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.rule_name
    

class Log(models.Model):
    log_id = models.AutoField(primary_key=True)  # Auto-increment ID
    user_id = models.CharField(max_length=255)  # User ID as a string
    action_type = models.CharField(max_length=100)  # e.g., "create_order", "update_profile"
    details = models.JSONField()  # JSON field to store extra details (requires PostgreSQL)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp when created

    def __str__(self):
        return f"Log {self.log_id} - {self.action_type} by User {self.user_id}"