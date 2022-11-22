from django.urls import path, include

from api.views import TaskDetailView, TaskUpdateView, TaskDeleteView, ProjectDetailView

urlpatterns = [
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
]
