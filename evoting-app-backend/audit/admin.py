from django.contrib import admin

from audit.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "action", "user", "details"]
    list_filter = ["action"]
    search_fields = ["user", "details", "action"]
    readonly_fields = ["timestamp", "action", "user", "details"]
    date_hierarchy = "timestamp"
