import os
from django.contrib import admin
from .models import Config


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        os.system("pm2 restart trading-bot")
        super(ConfigAdmin, self).save_model(request, obj, form, change)
