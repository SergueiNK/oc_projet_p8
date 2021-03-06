# Generated by Django 3.2.6 on 2021-12-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_product_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_url',
            new_name='individual_image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='list_image_url',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
    ]
