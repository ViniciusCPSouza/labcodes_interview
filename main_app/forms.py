"""
    The forms needed for the interaction between server and client.
"""

from django import forms
from djangular.forms import NgModelFormMixin
from main_app import models


class CommentForm(NgModelFormMixin, forms.ModelForm):

    class Meta:

        model = models.Comment
        fields = ("text", "author")


class TaskForm(NgModelFormMixin, forms.ModelForm):

    class Meta:

        model = models.Task
        fields = ("description", "done", "deadline", "comments")


class TODOListForm(NgModelFormMixin, forms.ModelForm):

    class Meta:

        model = models.TODOList
        fields = ("title", "tasks")