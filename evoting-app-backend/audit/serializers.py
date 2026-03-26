from rest_framework import serializers

from audit.models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
#  'id' and 'timestamp' are not set as read-only fields.
# These fields could be modified during write operations, which can corrupt audit data.
        fields = ["id", "timestamp", "action", "user_identifier", "details"]
        read_only_fields = ["id", "timestamp"]
