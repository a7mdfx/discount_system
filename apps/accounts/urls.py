from django.urls import path
from . import views

urlpatterns = [
    
    path('users/<int:user_id>/', views.get_user_profile, name='user-profile'),
    path('users/', views.get_user_list,name='user-list'),

]