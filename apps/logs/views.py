from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from apps.logs.models import Log
from apps.logs.serializers import LogSerializer

# Custom pagination class for better control
class LogPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # You can specify the page size in query parameters
    max_page_size = 100  # Maximum page size

class LogListView(generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = LogPagination
    filter_backends = (SearchFilter,)
    search_fields = ['user_id', 'action_type']  # Allow filtering by user_id and action_type

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get query parameters
        user_id = self.request.query_params.get('user_id', None)
        action_type = self.request.query_params.get('action_type', None)
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)

        # Apply filters based on query parameters
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if action_type:
            queryset = queryset.filter(action_type=action_type)
        if from_date and to_date:
            queryset = queryset.filter(created_at__range=[from_date, to_date])

        return queryset
    
    