# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(db_index=False, blank=True, unique=True)),
                ('url', models.URLField()),
                ('likes', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(verbose_name='date_joined', default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateTimeField(verbose_name='date_joined', default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
