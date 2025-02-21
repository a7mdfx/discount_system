from django.urls import path
from apps.discount.views import CalculateDiscountView


urlpatterns = [
    
    path('cart/calculate-discount/',CalculateDiscountView.as_view(), name='calculate-discount'),

]