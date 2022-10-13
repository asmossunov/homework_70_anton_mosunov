from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from tracker.models import Task
from tracker.forms import TaskForm


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskAddView(CreateView):
    template_name = 'add_task.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super(TaskAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = '/'
