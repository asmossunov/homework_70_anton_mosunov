from django.contrib import admin
from django.urls import path

from tracker.views.base import IndexView
from tracker.views.tasks import TaskView, TaskAddView, TaskUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('tasks/', IndexView.as_view(), name='index'),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('tasks/add/', TaskAddView.as_view(), name='task_add'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    # path('articles/<int:pk>/delete/', delete_view, name='article_delete'),
    # path('articles/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),


]
