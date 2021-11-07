import os

from django.contrib import admin
from .models import Service, ServiceItem


class ServiceItemInline(admin.StackedInline):
    model = ServiceItem
    classes = ['collapse']
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceItemInline]

    def save_model(self, request, obj, form, change):
        os.system("pm2 restart trading-worker")
        super(ServiceAdmin, self).save_model(request, obj, form, change)
