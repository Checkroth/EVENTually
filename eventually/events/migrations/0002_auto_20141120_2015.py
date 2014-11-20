# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 20, 20, 15, 22, 905349), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 20, 20, 15, 26, 957255)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_photo',
            field=models.ImageField(max_length=255, null=True, upload_to=b'events', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 20, 20, 15, 31, 385163)),
            preserve_default=False,
        ),
    ]
