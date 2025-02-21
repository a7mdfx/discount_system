from django.urls import path
from apps.accounts.views import UserListCreateView,UserProfileDetailView

urlpatterns = [
    
    path('users/<int:id>/', UserProfileDetailView.as_view(), name='user-profile'),
    path('users/', UserListCreateView.as_view(),name='user-list'),

]