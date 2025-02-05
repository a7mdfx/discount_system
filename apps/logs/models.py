from django.db import models

class Log(models.Model):
    log_id = models.AutoField(primary_key=True)  # Auto-increment ID
    user_id = models.CharField(max_length=255)  # User ID as a string
    action_type = models.CharField(max_length=100)  # e.g., "create_order", "update_profile"
    details = models.JSONField()  # JSON field to store extra details (requires PostgreSQL)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp when created

    def __str__(self):
        return f"Log {self.log_id} - {self.action_type} by User {self.user_id}"