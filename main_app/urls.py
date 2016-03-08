"""The custom urls module for the app."""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from main_app import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^todo_lists/$', views.TODOListList.as_view(), name="todo_list-list"),
    url(r'^todo_lists/(?P<pk>\d+)/$', views.TODOListDetail.as_view(), name="todo_list-detail"),
    url(r'^tasks/$', views.TaskList.as_view(), name="task-list"),
    url(r'^tasks/(?P<pk>\d+)/$', views.TaskDetail.as_view(), name="task-detail"),
    url(r'^comments/$', views.CommentList.as_view(), name="comment-list"),
    url(r'^comments/(?P<pk>\d+)/$', views.CommentDetail.as_view(), name="comment-detail"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
