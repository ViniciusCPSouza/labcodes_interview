"""The models module."""

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    """A comment that can be made in a task."""

    text = models.CharField("The content of the comment", max_length=600)
    author = models.ForeignKey(User)


class Task(models.Model):
    """A task that can have a deadline, comments and be finished."""

    description = models.CharField("The subject of the task", max_length=300)
    done = models.BooleanField("Whether or not the task is finished", default=False)
    deadline = models.DateTimeField("The deadline for this task", null=True, blank=True)
    comments = models.ManyToManyField(Comment)


class TODOList(models.Model):
    """A TODO list, which is a named list of tasks."""

    title = models.CharField("The title of the list", max_length=80)
    tasks = models.ManyToManyField(Task)
