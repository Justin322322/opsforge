from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    """Extended user profile for OpsForge"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(
        max_length=50,
        choices=[
            ('user', 'User'),
            ('admin', 'Admin'),
            ('support', 'Support'),
        ],
        default='user'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('pending', 'Pending'),
            ('inactive', 'Inactive'),
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.role}"

    class Meta:
        ordering = ['-created_at']


class AuditLog(models.Model):
    """Audit log for system actions"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=200)
    tool = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'


class FeatureFlag(models.Model):
    """Feature flags for gradual rollouts"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    exposure_percentage = models.IntegerField(default=0, help_text="Percentage of users (0-100)")
    environment = models.CharField(
        max_length=50,
        choices=[
            ('development', 'Development'),
            ('staging', 'Staging'),
            ('production', 'Production'),
        ],
        default='production'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('stable', 'Stable'),
            ('beta', 'Beta'),
            ('deprecated', 'Deprecated'),
        ],
        default='beta'
    )
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.exposure_percentage}%)"

    class Meta:
        ordering = ['-updated_at']


class QueueTask(models.Model):
    """Queue tasks for ops console"""
    queue_name = models.CharField(max_length=100)
    task_type = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='pending'
    )
    retry_count = models.IntegerField(default=0)
    auto_retry = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.queue_name} - {self.task_type}"

    class Meta:
        ordering = ['-created_at']


class Activity(models.Model):
    """Recent activity feed"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=200)
    tool = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.tool}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Activities'

