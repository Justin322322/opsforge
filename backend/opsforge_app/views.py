from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import UserProfile, AuditLog, FeatureFlag, QueueTask, Activity


def home(request):
    """Main landing page"""
    return render(request, 'index.html')


@require_http_methods(["GET"])
def tools_view(request):
    """HTMX view for tools list"""
    tag = request.GET.get('tag', 'all')
    
    # Filter tools based on tag if needed
    context = {
        'tag': tag,
    }
    return render(request, 'partials/tools.html', context)


@require_http_methods(["GET"])
def tool_user_admin(request):
    """HTMX view for user admin tool"""
    profiles = UserProfile.objects.select_related('user').all()[:10]
    context = {
        'profiles': profiles,
    }
    return render(request, 'partials/tool-user-admin.html', context)


@require_http_methods(["GET", "POST"])
def tool_audit_log(request):
    """HTMX view for audit log tool"""
    if request.method == 'POST':
        # Handle export or filter
        pass
    
    logs = AuditLog.objects.select_related('user').all()[:50]
    context = {
        'logs': logs,
        'total_count': AuditLog.objects.count(),
    }
    return render(request, 'partials/tool-audit-log.html', context)


@require_http_methods(["GET"])
def tool_feature_flags(request):
    """HTMX view for feature flags tool"""
    flags = FeatureFlag.objects.all()
    context = {
        'flags': flags,
    }
    return render(request, 'partials/tool-feature-flags.html', context)


@require_http_methods(["GET"])
def tool_ops_console(request):
    """HTMX view for ops console tool"""
    queues = QueueTask.objects.values('queue_name').annotate(
        pending_count=Count('id', filter=Q(status='pending'))
    )
    
    pending_tasks = QueueTask.objects.filter(status='pending')[:20]
    
    context = {
        'queues': queues,
        'pending_tasks': pending_tasks,
    }
    return render(request, 'partials/tool-ops-console.html', context)


@require_http_methods(["GET"])
def activity_view(request):
    """HTMX view for activity feed"""
    activities = Activity.objects.select_related('user').all()[:10]
    context = {
        'activities': activities,
    }
    return render(request, 'partials/activity.html', context)


@require_http_methods(["GET"])
def help_view(request):
    """HTMX view for help"""
    return render(request, 'partials/help.html')


# API endpoints for HTMX forms
@require_http_methods(["POST"])
def invite_user(request):
    """Handle user invitation form"""
    email = request.POST.get('email')
    role = request.POST.get('role', 'user')
    
    # TODO: Implement user creation logic
    # For now, just refresh the user list
    # In production, you would:
    # 1. Create or get user
    # 2. Create UserProfile
    # 3. Send invitation email
    # 4. Log the action
    
    # Return HTML fragment for HTMX to swap - return the updated table
    profiles = UserProfile.objects.select_related('user').all()[:10]
    return render(request, 'partials/tool-user-admin.html', {'profiles': profiles})

