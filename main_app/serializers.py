"""The serializers needed by the REST api."""

from django.contrib.auth import models as auth_models
from rest_framework import serializers
import dateutil.parser

import models as main_app_models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """The serializer class for the User model."""

    class Meta:
        """Meta class."""

        model = auth_models.User
        fields = ('pk', 'url', 'username', 'email', 'is_staff')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """The serializer class for the Comment model."""

    class Meta:
        """Meta class."""

        model = main_app_models.Comment
        fields = ('pk', 'text', 'author')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    """The serializer class for the Task model."""

    class Meta:
        """Meta class."""

        model = main_app_models.Task
        fields = ('pk', 'description', 'done', 'deadline', 'comments')

    def create(self, validated_data):

        deadline = validated_data.get('deadline', None)

        if deadline:

            validated_data.update('deadline', dateutil.parser.parse(deadline))

        print validated_data.keys()

        return main_app_models.Task.objects.create(**validated_data)

    def update(self, instance, validated_data):

        new_deadline = validated_data.get('deadline', None)

        if new_deadline:

            instance.deadline = dateutil.parser.parse(new_deadline)

        instance.description = validated_data.get('description', instance.description)
        instance.done = validated_data.get('done', instance.done)

        instance.save()

        return instance


class TODOListSerializer(serializers.HyperlinkedModelSerializer):
    """The serializer class for the TODOList model."""

    class Meta:
        """Meta class."""

        model = main_app_models.TODOList
        fields = ('pk', 'title', 'tasks')
