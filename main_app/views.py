import dateutil.parser
import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
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


@login_required
def home(request):

    context = {}
    return render(request, 'index.html', context)


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect("/")


def todo_list_form(request):

    if request.method == "POST":

        post_data = json.loads(request.body)

        if "id" in post_data:

            todo_list = main_app_models.TODOList.objects.get(pk=int(post_data["id"]))
            todo_list.title = post_data["title"]
            todo_list.save()

        else:

            main_app_models.TODOList(title=post_data["title"]).save()

    return HttpResponse()


def task_form(request):

    if request.method == "POST":

        post_data = json.loads(request.body)

        if "id" in post_data:

            task = main_app_models.Task.objects.get(pk=int(post_data["id"]))

            if "deadline" in post_data:

                task.deadline = dateutil.parser.parse(post_data["deadline"])

            if "description" in post_data:

                task.description = post_data["description"]

            if "done" in post_data:

                print post_data["done"]

                task.done = post_data["done"]

            task.save()

        else:

            params = dict()

            params["description"] = post_data["description"]

            if "deadline" in post_data:

                params["deadline"] = dateutil.parser.parse(post_data["deadline"])

            task = main_app_models.Task(**params)
            task.save()

            todo_list = main_app_models.TODOList.objects.get(pk=int(post_data["parent_list"]))
            todo_list.tasks.add(task)
            todo_list.save()

    return HttpResponse()


def comment_form(request):

    if request.method == "POST":

        post_data = json.loads(request.body)

        comment = main_app_models.Comment(text=post_data["text"], author=request.user)
        comment.save()

        parent_task = main_app_models.Task.objects.get(pk=int(post_data["parent_task"]))
        parent_task.comments.add(comment)
        parent_task.save()

    return HttpResponse()


def delete_task(request):

    if request.method == "POST":

        task = main_app_models.Task.objects.get(pk=int(json.loads(request.body)["id"]))

        for comment in task.comments.all():

            comment.delete()

        task.delete()

    return HttpResponse()


def delete_todo_list(request):

    if request.method == "POST":

        todo_list = main_app_models.TODOList.objects.get(pk=int(json.loads(request.body)["id"]))

        for task in todo_list.tasks.all():

            for comment in task.comments.all():

                comment.delete()

            task.delete()

        todo_list.delete()

    return HttpResponse()
