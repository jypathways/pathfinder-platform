# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spark',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.AlterField(
            model_name='spark',
            name='name',
            field=models.CharField(unique=True, max_length=128),
        ),
    ]
