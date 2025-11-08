from django.urls import path
from . import views

app_name = 'opsforge_app'

urlpatterns = [
    # HTMX partial views
    path('tools.html', views.tools_view, name='tools'),
    path('tool-user-admin.html', views.tool_user_admin, name='tool_user_admin'),
    path('tool-audit-log.html', views.tool_audit_log, name='tool_audit_log'),
    path('tool-feature-flags.html', views.tool_feature_flags, name='tool_feature_flags'),
    path('tool-ops-console.html', views.tool_ops_console, name='tool_ops_console'),
    path('activity.html', views.activity_view, name='activity'),
    path('help.html', views.help_view, name='help'),
    
    # API endpoints for forms
    path('invite-user/', views.invite_user, name='invite_user'),
]

