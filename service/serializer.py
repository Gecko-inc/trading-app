from rest_framework import serializers

from service.models import ServiceItem, Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            "key",
            "d_timeout",
            "w_timeout",
            "b_timeout",
            "bd_timeout",
            "rsi_d",
            "rsi_w",
            "rsi_b",
            "rsi_bd",
            "papers",
        ]
