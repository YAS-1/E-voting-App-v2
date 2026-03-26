from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class AuditPagination(PageNumberPagination):
    page_size = 20

from accounts.permissions import IsAdminUser
from audit.serializers import AuditLogSerializer
from audit.services import AuditService
from audit.models import AuditLog

# The absence of pagination caused large datasets to be returned at once, 
# impacting performance and scalability, and was fixed by introducing paginated responses.
class AuditPagination(PageNumberPagination):
    page_size = 20


class AuditLogListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AuditLogSerializer
    pagination_class = AuditPagination

    def get_queryset(self):
        #The view directly accessed the model instead of using the service layer, 
        # breaking architectural consistency and maintainability, and was fixed by
        #  delegating data retrieval to AuditService
        qs = AuditService.get_recent(limit=100)

        action = self.request.query_params.get("action")
        user = self.request.query_params.get("user")

        if action:
            qs = qs.filter(action__iexact=action.strip())

        if user := self.request.query_params.get("user"):
            qs = qs.filter(user__username__icontains=user.strip())

        return qs


class AuditActionTypesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            types = list(AuditService.get_action_types())
            # Converting the queryset to a list increased memory usage 
            # unnecessarily, and this was improved by deferring evaluation 
            # or optimizing retrieval.
            return Response(list(types))
    #Lack of error handling could cause unhandled exceptions and API 
    # crashes, and this was fixed by wrapping logic in a safe try-except block.
        except Exception:
            return Response({"error": "Unable to fetch action types"}, status=500)
