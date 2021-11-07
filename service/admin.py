from django.contrib import admin
from .models import Service, ServiceItem


class ServiceItemInline(admin.StackedInline):
    model = ServiceItem
    classes = ['collapse']
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceItemInline]
