# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tinylink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('long_url', models.CharField(max_length=2500, verbose_name='Long URL')),
                ('short_url', models.CharField(unique=True, max_length=32, verbose_name='Short URL')),
                ('is_broken', models.BooleanField(default=False, verbose_name='Status')),
                ('validation_error', models.CharField(default=b'', max_length=100, verbose_name='Validation Error')),
                ('last_checked', models.DateTimeField(default=datetime.datetime(2015, 6, 26, 21, 18, 13, 702405, tzinfo=utc), verbose_name='Last validation')),
                ('amount_of_views', models.PositiveIntegerField(default=0, verbose_name='Amount of views')),
                ('redirect_location', models.CharField(default=b'', max_length=2500, verbose_name='Redirect location')),
                ('user', models.ForeignKey(related_name='tinylinks', verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
