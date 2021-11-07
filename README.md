# Установка

## Системные требования
OS Linux
Python 3.7+
База данных: PostgreSQL или SQLite

## PM2
Выполним следющие команды:
```
sudo apt install nodejs

sudo apt install npm

npm install pm2 -g
```
## Виртуальное окружение
Переходим в папку проекта
cd path/to/bot/
Чтобы создать виртуальное окружение, выполняем следующие команды:
```
python3 -m pip install --upgrade pip
pip3 install virtualenv
python3 -m venv env
```
Активируем наше виртуальное окружение:
``` . env/bin/activate ```

Установим модули:
```pip install -r requirements.txt```

## Подключение
Создайте папку local
В нее поместите файл config.json
в config.json Запишем следующее:
```
{
    "secret_key": "sectet_key",
    "db_type": "psql",
    "database": "db_name",
    "user": "db_user",
    "host": "localhost",
    "password": "db_password",
    "port": "1234",
    "url": "ip_вашего_сервера:8000"
}
```

## Настройка ботов
Пропишите команды:
```
python manage.py migrate

python manage.py default_data
```
Далее создадим администратора 
```
python manage.py createsuperuser
```
Указываем имя пользователя, почту и пароль

## Запуск
Пропишите команду

```
pm2 start project.json
```

Если вы все сделали правильно, то по адресу http://ip_адрес_сервера:8000/admin/ , у вас откроется админ панель бота

## Рестарт
После того, как вы подставите свои токены ботов, пропишите ```pm2 restart all```
