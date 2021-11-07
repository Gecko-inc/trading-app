from django.urls import path

from telegram.views import Start

app_name = 'telegram'

urlpatterns = [
    path('start/', Start.as_view()),
]
