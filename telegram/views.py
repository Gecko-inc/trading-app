from rest_framework.response import Response
from rest_framework.views import APIView
import telebot
from telebot import types
import threading

from config.func import parser
from config.models import Config
from service.models import Service
from telegram.models import User


class Start(APIView):

    def post(self, request):
        """
          Создание пользователя
        """
        data = request.data
        bot = telebot.TeleBot(Config.objects.get(key='bot_token').value)
        menu = types.ReplyKeyboardMarkup(True, False)
        menu.row("Получить информацию")
        bot.send_message(data.get("id"), Config.objects.get(key='hello_text').value, reply_markup=menu)
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


class InfoView(APIView):
    def get(self, request):
        try:
            user = User.objects.get(telegram_id=request.GET.get("id"))
            try:
                service = Service.objects.get(key='service_screener', is_active=True)
            except Service.DoesNotExist:
                return Response(status=404)
            if user.is_active:
                threading.Thread(target=parser, name="D parser",
                                 args=(service.rsi_d, service.papers(), "d", user.telegram_id)).start()
                threading.Thread(target=parser, name="W parser",
                                 args=(service.rsi_w, service.papers(), "w", user.telegram_id)).start()
                threading.Thread(target=parser, name="B parser",
                                 args=(service.rsi_b, service.papers(), "bw", user.telegram_id)).start()
                threading.Thread(target=parser, name="B parser",
                                 args=(service.rsi_bd, service.papers(), "bd", user.telegram_id)).start()
                return Response(status=200)
            return Response(status=401)
        except User.DoesNotExist:
            return Response(status=404)
