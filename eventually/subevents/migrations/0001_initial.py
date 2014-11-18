# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subevent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('main_event', models.ForeignKey(to='events.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
