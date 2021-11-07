from rest_framework import serializers

from service.models import ServiceItem, Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            "key",
            "d_timeout",
            "w_timeout",
            "rsi_d",
            "rsi_w",
            "papers",
        ]
