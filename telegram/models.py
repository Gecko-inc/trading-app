import telebot
from django.db import models

from config.models import Config


class User(models.Model):
    username = models.CharField("Логин пользователя", max_length=130, blank=True, default='None')
    telegram_id = models.CharField("ID пользователя", unique=False, max_length=130)
    is_active = models.BooleanField("Активен", default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"@{self.username}" if self.username else self.telegram_id

    @classmethod
    def whitelist(cls, text: str):
        bot = telebot.TeleBot(Config.objects.get(key="bot_token").value)
        for user in cls.objects.filter(is_active=True):
            try:
                print(user.telegram_id)
                bot.send_message(user.telegram_id, text=text)
            except Exception as e:
                print(e)


# Опросы
class Poll(models.Model):
    title = models.CharField("Название", max_length=130)
    text = models.TextField("Текст опроса")
    is_send = models.BooleanField("Отправлено", default=False)

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.title

    def get_vote(self):
        text = ""
        for vote in self.button.all():
            text += f"За '{vote.title}' проголосовало {vote.vote} человек\n"

        return text

    def get_total_vote(self):
        total = 0
        for vote in self.button.all():
            total += vote.vote

        return f"проголосовало {total} человек"


class PollButton(models.Model):
    poll = models.ForeignKey(Poll, verbose_name="Опрос", related_name="button", on_delete=models.CASCADE)
    title = models.CharField("Ответ", max_length=130)
    vote = models.IntegerField("Голоса", default=0)

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = 'Варианты ответов'

    def __str__(self):
        return self.title
