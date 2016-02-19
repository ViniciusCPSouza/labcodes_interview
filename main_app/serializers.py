"""
    The serializers needed by the REST api.
"""

from django.contrib.auth import models as auth_models
from rest_framework import serializers

import models as main_app_models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = auth_models.User
        fields = ('url', 'username', 'email', 'is_staff')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = main_app_models.Comment
        fields = ('text', 'author')


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = main_app_models.Task
        fields = ('description', 'done', 'deadline', 'comments')


class TODOListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = main_app_models.TODOList
        fields = ('title', 'tasks')
