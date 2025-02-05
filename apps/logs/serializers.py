from rest_framework import serializers
from .models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['log_id', 'user_id', 'action_type', 'details', 'created_at']