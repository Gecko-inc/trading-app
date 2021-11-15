from django.urls import path

from telegram.views import Start, InfoView

app_name = 'telegram'

urlpatterns = [
    path('start/', Start.as_view()),
    path('info/', InfoView.as_view()),
]
