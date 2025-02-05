from django.urls import path
from . import views


urlpatterns = [
    
    path('orders/', views.OrderListView.as_view(), name='order-list'),  # GET/POST all orders
    path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order-detail'),  # GET/PUT/DELETE specific order
    path('users/<int:user_id>/orders/', views.UserOrdersHistoryView.as_view(), name='user-orders-history'),
   
]