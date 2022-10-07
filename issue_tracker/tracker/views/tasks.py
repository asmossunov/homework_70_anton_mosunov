from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from tracker.models import Task
from tracker.forms import TaskForm


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskAddView(CreateView):
    form_class = TaskForm
    template_name = 'add_task.html'


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = '/tasks/'
