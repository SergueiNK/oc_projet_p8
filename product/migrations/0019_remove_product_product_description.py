# Generated by Django 3.2.6 on 2021-11-05 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_description',
        ),
    ]
