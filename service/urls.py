from django.urls import path

from service.views import ServiceView

app_name = 'service'

urlpatterns = [
    path("service/", ServiceView.as_view())
]
