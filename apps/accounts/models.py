# accounts/models.py
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