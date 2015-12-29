# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True, db_index=False, blank=True)),
                ('url', models.URLField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('author', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='trail.Category', default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_joined', models.DateTimeField(verbose_name='date_joined', default=django.utils.timezone.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
