# Generated by Django 4.2.3 on 2023-08-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartsystem', '0010_alter_cart_options_remove_cart_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]