# Generated by Django 3.1.7 on 2021-05-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0002_auto_20210527_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=130, verbose_name='Логин пользователя'),
        ),
    ]
