"""The views module."""

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth import models as auth_models
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from serializers import CommentSerializer, TaskSerializer, TODOListSerializer, UserSerializer
from models import Comment, Task, TODOList


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = auth_models.User.objects.all()
    serializer_class = UserSerializer


class CommentList(ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TaskList(ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TODOListList(ListCreateAPIView):

    queryset = TODOList.objects.all()
    serializer_class = TODOListSerializer


class TODOListDetail(RetrieveUpdateDestroyAPIView):

    queryset = TODOList.objects.all()
    serializer_class = TODOListSerializer


def logout(request):
    """Log out user."""
    auth_logout(request)
    return redirect("/")
