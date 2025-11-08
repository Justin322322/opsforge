"""
URL configuration for opsforge project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from opsforge_app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path('partials/', include('opsforge_app.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

