# Generated by Django 4.2.1 on 2023-06-18 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 18, 16, 35)),
        ),
        migrations.AddField(
            model_name='vendor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]