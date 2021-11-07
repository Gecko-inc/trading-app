# Generated by Django 3.1.6 on 2021-11-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20211107_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='rsi_d',
            field=models.CharField(default='20', max_length=130, verbose_name='RSI дневной'),
        ),
        migrations.AddField(
            model_name='service',
            name='rsi_w',
            field=models.CharField(default='25', max_length=130, verbose_name='RSI недельный'),
        ),
    ]
