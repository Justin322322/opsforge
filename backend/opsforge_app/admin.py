from django.contrib import admin
from .models import UserProfile, AuditLog, FeatureFlag, QueueTask, Activity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'status', 'created_at']
    list_filter = ['role', 'status']
    search_fields = ['user__email', 'user__username']


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action', 'tool', 'user', 'created_at']
    list_filter = ['tool', 'created_at']
    search_fields = ['action', 'tool', 'user__email']
    readonly_fields = ['created_at']


@admin.register(FeatureFlag)
class FeatureFlagAdmin(admin.ModelAdmin):
    list_display = ['name', 'exposure_percentage', 'environment', 'status', 'enabled']
    list_filter = ['environment', 'status', 'enabled']
    search_fields = ['name', 'description']


@admin.register(QueueTask)
class QueueTaskAdmin(admin.ModelAdmin):
    list_display = ['queue_name', 'task_type', 'status', 'retry_count', 'created_at']
    list_filter = ['status', 'queue_name', 'auto_retry']
    search_fields = ['queue_name', 'task_type']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['action', 'tool', 'user', 'created_at']
    list_filter = ['tool', 'created_at']
    search_fields = ['action', 'tool', 'user__email']
    readonly_fields = ['created_at']

