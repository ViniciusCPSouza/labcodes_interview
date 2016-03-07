"""The custom urls module for the app."""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from main_app import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^todo_lists/$', views.todo_list_list, name="todo_list-list"),
    url(r'^todo_lists/(?P<pk>\d+)/$', views.todo_list_detail, name="todo_list-detail"),
    url(r'^tasks/$', views.task_list, name="task-list"),
    url(r'^tasks/(?P<pk>\d+)/$', views.task_detail, name="task-detail"),
    url(r'^comments/$', views.comment_list, name="comment-list"),
    url(r'^comments/(?P<pk>\d+)/$', views.comment_detail, name="comment-detail"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
