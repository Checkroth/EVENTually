# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_event_inviter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attending', models.CharField(default=b'?', max_length=1, verbose_name=b'Will you be attending', choices=[(b'?', b''), (b'Y', b'Yes'), (b'N', b'No')])),
                ('event', models.ForeignKey(related_name='invite_event', to='events.Event')),
                ('user', models.ForeignKey(related_name='invite_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='event',
            name='guests',
        ),
        migrations.AlterField(
            model_name='event',
            name='inviter',
            field=models.CharField(default=b'HOST', max_length=255, verbose_name=b'Who can invite guests', choices=[(b'HOST', b'Just me'), (b'GUESTS', b'Guests & me'), (b'EVERYONE', b'Everyone')]),
            preserve_default=True,
        ),
    ]
