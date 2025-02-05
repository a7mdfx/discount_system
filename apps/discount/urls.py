from django.urls import path
from . import views


urlpatterns = [
    
    path('cart/calculate-discount/', views.CalculateDiscountView.as_view(), name='calculate-discount'),

]