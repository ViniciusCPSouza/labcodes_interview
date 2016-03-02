"""The custom urls module for the app."""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from main_app import views


router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'todo_lists', views.TODOListViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
