from rest_framework.response import Response
from rest_framework.views import APIView
import telebot
from telebot import types

from config.models import Config
from telegram.models import User


class Start(APIView):

    def post(self, request):
        """
          Создание пользователя
        """
        data = request.data
        bot = telebot.TeleBot(Config.objects.get(key='bot_token').value)
        bot.send_message(data.get("id"), Config.objects.get(key='hello_text').value)
        try:
            User.objects.get(telegram_id=data.get('id'))
        except User.DoesNotExist:
            if data.get("username"):
                User(
                    username=data.get('username'),
                    telegram_id=data.get('id'),
                ).save()
            else:
                User(
                    telegram_id=data.get('id'),
                ).save()
        return Response(
            status=200
        )
