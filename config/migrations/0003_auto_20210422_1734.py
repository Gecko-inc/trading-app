# Generated by Django 3.1.6 on 2021-04-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20210422_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='key',
            field=models.CharField(help_text='Служебное поле', max_length=130, unique=True, verbose_name='Ключ'),
        ),
    ]
