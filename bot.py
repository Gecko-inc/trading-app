# Импорт модулей
import telebot
from telebot import types
import requests
import json
from pathlib import Path
import time
import sys

# Подключение файла настроек
BASE_DIR = Path(__file__).resolve().parent.parent
try:
    with open('local/config.json') as handle:
        config = json.load(handle)
except IOError:
    config = {
        'url': 'http://127.0.0.1:8000',
    }

# Константы
url = config['url']
toolbar_width = 40

# Даем время, чтобы запустился Django
# sys.stdout.write("Starting bot\n%s" % (" " * toolbar_width))
# sys.stdout.flush()
# sys.stdout.write("\b" * (toolbar_width + 1))
# for i in range(toolbar_width):
#     time.sleep(0.1)
#     sys.stdout.write("█")
#     sys.stdout.flush()
# sys.stdout.write("\nSuccess\n")

r = requests.get(f"{url}/token/")  # Получение токена
token = r.json().get("token")
admin_id = r.json().get("admin_id", '0')
bot = telebot.TeleBot(token)

print(f"""

░██████╗░███████╗░█████╗░██╗░░██╗░█████╗░
██╔════╝░██╔════╝██╔══██╗██║░██╔╝██╔══██╗
██║░░██╗░█████╗░░██║░░╚═╝█████═╝░██║░░██║
██║░░╚██╗██╔══╝░░██║░░██╗██╔═██╗░██║░░██║
╚██████╔╝███████╗╚█████╔╝██║░╚██╗╚█████╔╝
░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░

    Информация о боте:
Имя бота: @{bot.get_me().username}
токен: {token}
URL-адрес для API: {config.get('url')}
Папка проекта: {BASE_DIR}
©nicstim
    """)


@bot.message_handler(commands=['start'])
def start(message):
    requests.post(f"{url}/api/start/", data={
        "id": message.from_user.id,
        'username': message.from_user.username
    })


@bot.message_handler(commands=['cart'])
def get_cart(message):
    requests.get(f"{url}/api/cart/?user={message.chat.id}")


@bot.message_handler(content_types=['text'])
def body(message):
    pass


# Обработка локации
@bot.message_handler(content_types=['location'])
def user(local):
    pass


@bot.edited_message_handler(content_types=['location'])
def user(local):
    pass


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    pass


bot.skip_pending = True
bot.polling(none_stop=True, interval=0)
