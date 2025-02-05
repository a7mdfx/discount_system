from django.urls import path
from . import views


urlpatterns = [
    
    path('logs/', views.LogListView.as_view(), name='log-list'),  # NEW ENDPOINT
]