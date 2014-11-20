# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20141120_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(related_name='event_guests', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
