# Generated by Django 3.2.6 on 2021-10-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_code_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_product',
            field=models.IntegerField(unique=True, verbose_name='code of product'),
        ),
    ]
