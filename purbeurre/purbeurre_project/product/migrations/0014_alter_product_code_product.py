# Generated by Django 3.2.6 on 2021-10-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_code_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_product',
            field=models.CharField(max_length=100, verbose_name='code of product'),
        ),
    ]