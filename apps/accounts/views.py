from rest_framework import generics
from apps.accounts.models import UserProfile
from rest_framework.response import Response
from apps.accounts.serializers import UserProfileSerializer

# Retrieve single user profile
class UserProfileDetailView(generics.RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'  # Default is 'pk', but we specify 'id' for clarity

# List all user profiles
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

