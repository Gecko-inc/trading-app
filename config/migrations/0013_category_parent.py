# Generated by Django 3.1.6 on 2021-10-20 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0012_auto_20211018_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='config.category', verbose_name='Родительская категория'),
        ),
    ]
