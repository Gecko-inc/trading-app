# Generated by Django 3.1.6 on 2021-04-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='title',
            field=models.CharField(max_length=130, unique=True, verbose_name='Наименование кнопки'),
        ),
    ]
