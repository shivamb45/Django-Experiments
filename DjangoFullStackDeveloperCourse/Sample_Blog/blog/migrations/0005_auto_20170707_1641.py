# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 11:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170707_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 7, 11, 11, 19, 852240, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 7, 11, 11, 19, 851486, tzinfo=utc)),
        ),
    ]
