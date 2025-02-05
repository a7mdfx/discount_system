from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.accounts.serializers import UserProfileSerializer
from apps.accounts.models import UserProfile

from rest_framework import generics

# View to get user profile details
class UserProfileDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@api_view(['GET'])
def get_user_profile(request, user_id):
    try:
        user_profile_object = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        return Response(
            data={
                "message": "User not found"
            },
            status=404
        )

    serializer = UserProfileSerializer(instance=user_profile_object)
    user_profile_data = serializer.data

    return Response(
        data=user_profile_data,
        status=200
    )

@api_view(['GET'])
def get_user_list(request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data, status=200)


