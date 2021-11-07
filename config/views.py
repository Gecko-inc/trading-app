from rest_framework.response import Response
from rest_framework.views import APIView
from pathlib import Path

from .models import Config
import telebot


def send_msg(chats, message, token):
    """
      Функция рассылки
    """
    home = Path(__file__).resolve().parent.parent
    bot = telebot.TeleBot(token)
    for chat in chats:
        try:
            if message.image:
                with open(f"{home}{message.image.url}", "rb") as photo:
                    bot.send_photo(chat.telegram_id, photo, caption=message.text)
            else:
                bot.send_message(chat.telegram_id, text=message.text)
            if message.file:
                with open(f"{home}{message.file.url}", "rb") as photo:
                    bot.send_document(chat.telegram_id, data=photo)
        except Exception as e:
            print(e)


class GetToken(APIView):
    def get(self, request):
        """
          Получение токена бота
        """
        return Response({
            "token": Config.objects.get(key="bot_token").value,
        })
