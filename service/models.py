from django.db import models
from django.utils import timezone


class Service(models.Model):
    title = models.CharField("Название", max_length=130)
    is_active = models.BooleanField("Активен", default=True)
    key = models.CharField("Ключ", max_length=130, help_text="Служебное поле.", unique=True)
    d_timeout = models.IntegerField("Частота обновления", default=30, help_text="В минутах")
    w_timeout = models.IntegerField("Частота обновления", default=10080, help_text="В минутах")
    rsi_d = models.CharField("RSI дневной", max_length=130, default='20')
    rsi_w = models.CharField("RSI недельный", max_length=130, default='25')
    start_time = models.TimeField("Время работы с", default=timezone.now)
    end_time = models.TimeField("Время работы до", default=timezone.now)

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __str__(self):
        return self.title

    def papers(self):
        return [item.title for item in self.items.all()]


class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="items")
    title = models.CharField("Наименование", max_length=330, help_text="Название акции или URL")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.title
