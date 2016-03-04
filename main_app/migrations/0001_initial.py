"""The migration module."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    """A migration class."""

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=600,
                                          verbose_name='The content of the comment')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=300,
                                                 verbose_name='The subject of the task')),
                ('done', models.BooleanField(default=False,
                                             verbose_name='Whether or not the task is finished')),
                ('deadline', models.DateTimeField(null=True,
                                                  verbose_name='The deadline for this task',
                                                  blank=True)),
                ('comments', models.ManyToManyField(to='main_app.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='TODOList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                        primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='The title of the list')),
                ('tasks', models.ManyToManyField(to='main_app.Task')),
            ],
        ),
    ]
