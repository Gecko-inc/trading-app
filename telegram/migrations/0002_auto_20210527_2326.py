# Generated by Django 3.1.7 on 2021-05-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, max_length=130, verbose_name='Номер подразделения'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=130, verbose_name='Роль в команде'),
        ),
    ]
