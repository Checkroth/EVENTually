# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('subevents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subevent',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 25, 2, 10, 19, 776414), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subevent',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 25, 2, 10, 25, 184828)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subevent',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 25, 2, 10, 29, 758623)),
            preserve_default=False,
        ),
    ]
