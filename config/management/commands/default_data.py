from django.core.management.base import BaseCommand

from config.models import Config


class Command(BaseCommand):
    help = "Добавляем стандартные данные в админку"

    def handle(self, *args, **options):
        print("""
            Добавляем данные по умолчанию.
            
            ©nicstim
        """)
        configs = [
            Config(
                title='Токен telegram бота',
                description="""Токен, который будет использоваться ботом""",
                key="bot_token",
                value='1381042876:AAEJcba_p5i-Wzos15Q7kJz04sSiFh4MZ_Q'
            ),
            Config(
                title='Приветствие',
                description="""/start""",
                key="hello_text",
                value="""
Добро пожаловать!
                """
            ),
        ]
        for config in configs:
            config.save()
        print("Данные заполнены.")
