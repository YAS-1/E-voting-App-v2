from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdminUser
from audit.serializers import AuditLogSerializer
from audit.services import AuditService
from audit.models import AuditLog


class AuditLogListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AuditLogSerializer

    def get_queryset(self):
        # Using get_recent(limit=None) may cause unclear slicing behavior.
        # Instead, query and filter directly improve performance and clarity.
        qs = AuditLog.objects.all().order_by("-timestamp")

        if action := self.request.query_params.get("action"):
            qs = qs.filter(action=action)
        if user := self.request.query_params.get("user"):
            qs = qs.filter(user_identifier__icontains=user)

        return qs


class AuditActionTypesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        types = list(AuditService.get_action_types())
        return Response(types)
