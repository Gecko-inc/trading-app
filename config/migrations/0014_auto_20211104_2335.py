# Generated by Django 3.1.6 on 2021-11-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0013_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
