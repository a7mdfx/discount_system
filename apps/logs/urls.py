from django.urls import path
from apps.logs.views import LogListView

urlpatterns = [
    
    path('logs/',LogListView.as_view(), name='log-list'),  # NEW ENDPOINT
]
