from audit.models import AuditLog


class AuditService:
    @staticmethod
    def log(action, user_identifier, details=""):
        #Added error handling becLogging should NEVER break core functionality
        try:
            return AuditLog.objects.create(
                action=action,
                user_identifier=user_identifier,
                details=details,
            )
        except Exception:
            # Fail silently to avoid breaking main functionality if audit logging fails
            return None

    @staticmethod
    def get_recent(limit=20):
        # get_recent() does not order results by timestamp.
        #The Returned logs may not be the most recent, making the method misleading.
        #Used .order_by("-timestamp") to ensure newest logs come first.
        return AuditLog.objects.all().order_by("-timestamp")[:limit]

    @staticmethod
    def filter_by_action(action_type):
        # audit log queries return records without timestamp ordering,causing logs to appear in an inconsistent sequence that misleads debugging 
        # and event interpretation, and it is fixed by explicitly ordering results by descending timestamp using .order_by
        return AuditLog.objects.filter(action=action_type).order_by("-timestamp")

    @staticmethod
    def filter_by_user(user_identifier):
        return AuditLog.objects.filter(user_identifier__icontains=user_identifier).order_by("-timestamp")

    @staticmethod
    def get_action_types():
        return (
            AuditLog.objects.values_list("action", flat=True).distinct()
            .distinct()
            .order_by("action")
        )
