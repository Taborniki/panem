# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161018153756 on 2016-11-23 18:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0061_auto_20161117_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timeOrdered',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='timePickup',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]