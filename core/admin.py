from django.contrib import admin

from core.models import UserProfile
from core.models import Order
from core.models import Discount


admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(Discount)
