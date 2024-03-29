# Generated by Django 3.1.6 on 2021-11-09 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20211107_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время работы до'),
        ),
        migrations.AddField(
            model_name='service',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время работы с'),
        ),
    ]
