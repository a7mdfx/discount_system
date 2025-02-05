from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Log
from .serializers import LogSerializer

class LogListView(APIView):
    def get(self, request):
        # Query Parameters
        user_id = request.query_params.get('user_id', None)
        action_type = request.query_params.get('action_type', None)
        from_date = request.query_params.get('from_date', None)
        to_date = request.query_params.get('to_date', None)

        # Base QuerySet
        logs = Log.objects.all()

        # Filtering
        if user_id:
            logs = logs.filter(user_id=user_id)
        if action_type:
            logs = logs.filter(action_type=action_type)
        if from_date and to_date:
            logs = logs.filter(created_at__range=[from_date, to_date])

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = request.query_params.get('limit', 10)  # Default limit to 10
        result_page = paginator.paginate_queryset(logs, request)

        # Serialize Data
        serializer = LogSerializer(result_page, many=True)

        # Response
        return paginator.get_paginated_response(serializer.data)
    


def create_log(user_id, action_type, details):
    Log.objects.create(
        user_id=user_id,
        action_type=action_type,
        details=details
    )
