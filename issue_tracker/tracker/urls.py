from django.contrib import admin
from django.urls import path

from tracker.views.base import TasksIndexView, ProjectsIndexView
from tracker.views.tasks import TaskView, TaskAddView, TaskUpdateView, TaskDeleteView
from tracker.views.projects import ProjectView, ProjectCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TasksIndexView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('articles/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

    path('', ProjectsIndexView.as_view(), name='index'),
    path('projects/', ProjectsIndexView.as_view(), name='index'),
    path('projects/<int:pk>', ProjectView.as_view(), name='project_detail'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_create'),

]
