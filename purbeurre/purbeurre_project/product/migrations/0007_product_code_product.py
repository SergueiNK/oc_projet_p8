# Generated by Django 3.2.6 on 2021-10-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20211022_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code_product',
            field=models.IntegerField(default='0', unique=True, verbose_name='code of product'),
        ),
    ]
