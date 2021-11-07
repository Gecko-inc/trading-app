from django.contrib import admin
from .models import User, Poll, PollButton
from config.models import Config

import telebot
from telebot import types


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основная информация', ({'fields': ('username', 'telegram_id')})),
        ('Доплнительная информация', ({'fields': ('owner', 'bonus')})),
    )


class PollButtonInline(admin.StackedInline):
    extra = 0
    model = PollButton
    readonly_fields = ("vote",)


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "is_send")
    actions = ["send_poll"]
    inlines = [PollButtonInline, ]
    readonly_fields = ('is_send',)
    fieldsets = (('Основная информация', ({'fields': ('title', 'text')})),
                 ("Дополнительная информация", ({'fields': ('is_send',)})),
                 )

    def send_poll(self, request, queryset):

        bot = telebot.TeleBot(Config.objects.get(key="bot_token").value)
        for obj in queryset:
            if not obj.user.all():
                poll = types.InlineKeyboardMarkup(row_width=1)
                for button in obj.button.all():
                    b = types.InlineKeyboardButton(text=button.title, callback_data=f"poll{button.id}")
                    poll.add(b)
                for user in User.objects.all():
                    bot.send_message(user.telegram_id, text=obj.text, reply_markup=poll)
            if obj.user.all():
                users = obj.user.all()
                poll = types.InlineKeyboardMarkup(row_width=1)
                for button in obj.button.all():
                    b = types.InlineKeyboardButton(text=button.title, callback_data=f"poll{button.id}")
                    poll.add(b)
                for user in users:
                    chat = User.objects.get(id=user.user_id)
                    bot.send_message(chat.telegram_id, text=obj.text, reply_markup=poll)
        queryset.update(is_send=True)

    send_poll.short_description = "Отправить опрос"
