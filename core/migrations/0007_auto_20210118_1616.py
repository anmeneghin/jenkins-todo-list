# Generated by Django 2.1.7 on 2021-01-18 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210118_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 18, 16, 16, 55, 839930)),
        ),
    ]
