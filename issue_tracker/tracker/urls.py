from django.contrib import admin
from django.urls import path

from tracker.views.base import TasksIndexView, ProjectsIndexView
from tracker.views.tasks import TaskView, TaskAddView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectsIndexView.as_view(), name='index'),
    path('tasks/', TasksIndexView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('articles/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),



]
