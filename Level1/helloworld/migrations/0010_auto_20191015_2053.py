# Generated by Django 2.2.5 on 2019-10-15 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0009_auto_20191015_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 19, 53, 31, 906810, tzinfo=utc)),
        ),
    ]
