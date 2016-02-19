from django.http import HttpResponse
from django.contrib.auth import models as auth_models
from rest_framework import viewsets
import serializers

import models as main_app_models


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = auth_models.User.objects.all()
    serializer_class = serializers.UserSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = main_app_models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class TaskViewSet(viewsets.ModelViewSet):

    queryset = main_app_models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TODOListViewSet(viewsets.ModelViewSet):

    queryset = main_app_models.TODOList.objects.all()
    serializer_class = serializers.TODOListSerializer


def home(request):

    return HttpResponse("")