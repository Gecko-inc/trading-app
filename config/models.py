from django.db import models


class Config(models.Model):
    title = models.CharField("Название", max_length=130)
    description = models.TextField("Описание", blank=True)
    key = models.CharField("Ключ", max_length=130, help_text="Служебное поле", unique=True)
    value = models.TextField("Значение", max_length=400, help_text='Максимум 400 символов.')

    class Meta:
        verbose_name = "Настройку"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.title
