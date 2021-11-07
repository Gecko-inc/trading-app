from django.urls import path
from .views import *

app_name = 'config'

urlpatterns = [
    path("token/", GetToken.as_view()),
]
