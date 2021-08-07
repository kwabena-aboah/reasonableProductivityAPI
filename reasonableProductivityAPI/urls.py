from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from task.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('task.urls')),
    path('', home, name='index'),
    path('api/users/', include('users.urls')),
    # path('api/user-profile/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
