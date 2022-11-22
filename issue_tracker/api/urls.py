from django.urls import path, include

from api.views import TaskDetailView, TaskUpdateView

urlpatterns = [
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    # path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_detail'),
]
