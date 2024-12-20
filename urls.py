from django.urls import path

from .views import TaskListView, TaskViewSet

urlpatterns = [
    path('list/', TaskListView.as_view()),
    path('CRUD/', TaskViewSet.as_view())
]