from django.urls import path
from apps.orders.views import OrderListView, OrderDetailView, UserOrdersHistoryView


urlpatterns = [
    
    path('orders/',OrderListView.as_view(), name='order-list'),  # GET/POST all orders
    path('orders/<int:order_id>/',OrderDetailView.as_view(), name='order-detail'),  # GET/PUT/DELETE specific order
    path('users/<int:user_id>/orders/',UserOrdersHistoryView.as_view(), name='user-orders-history'),
   
]