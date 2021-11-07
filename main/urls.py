from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('telegram.urls', namespace='telegram')),
    path('', include('config.urls', namespace='config')),
    path('', include('service.urls', namespace='service')),
]