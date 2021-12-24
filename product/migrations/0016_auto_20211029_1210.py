# Generated by Django 3.2.6 on 2021-10-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20211029_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code_product',
            field=models.CharField(max_length=500, unique=True, verbose_name='code of product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutrition_grade',
            field=models.CharField(max_length=500, verbose_name='nutrition grade of product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=500, verbose_name='name of product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.CharField(max_length=500, verbose_name='url of product'),
        ),
    ]