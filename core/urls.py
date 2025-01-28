# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('users/<int:user_id>/', views.get_user_profile, name='user-profile'),
    path('users/', views.get_user_list,name='user-list'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),  # GET/POST all orders
    path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order-detail'),  # GET/PUT/DELETE specific order
    path('users/<int:user_id>/orders/', views.UserOrdersHistoryView.as_view(), name='user-orders-history'),
    path('cart/calculate-discount/', views.CalculateDiscountView.as_view(), name='calculate-discount'),
    path('logs/', views.LogListView.as_view(), name='log-list'),  # NEW ENDPOINT
]
