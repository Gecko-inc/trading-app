import datetime

import telebot
from rest_framework.response import Response
from rest_framework.views import APIView

from config.models import Config
from service.models import Service
from service.serializer import ServiceSerializer
from telegram.models import User


class ServiceView(APIView):
    def get(self, request):
        if request.GET.get("key"):
            try:
                queryset = Service.objects.get(key=request.GET.get("key"), is_active=True)
                return Response(ServiceSerializer(queryset, many=False).data)
            except Service.DoesNotExist:
                return Response(status=404)
        queryset = Service.objects.filter(is_active=True)
        return Response(ServiceSerializer(queryset, many=True).data)

    def post(self, request):
        data = request.data
        paper = data.get("paper")
        try:
            service = Service.objects.get(key='service_screener', is_active=True)
        except Service.DoesNotExist:
            return Response(status=404)
        print(datetime.datetime.now().time())
        print(service.start_time)
        print(service.end_time)
        if service.start_time < datetime.datetime.now().time() < service.end_time:
            print('success')
            text = "hello world!"
            if data.get("period") == "w":
                text = f"💹Недельный RSI упал ниже {service.rsi_w} у акции {paper}"
            if data.get("period") == "d":
                text = f"💹Дневной RSI упал ниже {service.rsi_d} у акции {paper}"
            if data.get("period") == "bw":
                text = f"🛑Недельный RSI выше {service.rsi_b} у акции {paper[1]}"
            if data.get("period") == "bd":
                text = f"🛑Дневной RSI выше {service.rsi_bd} у акции {paper[1]}"
            User.whitelist(text=text)
            return Response(status=200)
        return Response(status=301)
