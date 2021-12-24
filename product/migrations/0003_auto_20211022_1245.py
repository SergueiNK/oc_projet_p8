# Generated by Django 3.2.6 on 2021-10-22 10:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_auto_20211022_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='product_fk',
            new_name='product_fk_id',
        ),
        migrations.RenameField(
            model_name='favorite',
            old_name='user_fk',
            new_name='user_fk_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_fk',
            new_name='category_fk_id',
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('product_fk_id', 'user_fk_id')},
        ),
    ]