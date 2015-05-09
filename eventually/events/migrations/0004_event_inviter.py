# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141120_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='inviter',
            field=models.CharField(default=b'HOST', max_length=255, choices=[(b'HOST', b'Just me'), (b'GUESTS', b'Guests & me'), (b'EVERYONE', b'Everyone')]),
            preserve_default=True,
        ),
    ]
