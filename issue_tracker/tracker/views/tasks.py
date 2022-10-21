from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from tracker.models import Task
from tracker.forms import TaskForm


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


class TaskView(DetailView):
    template_name = 'task/task.html'
    model = Task

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        queryset = Task.objects.filter(pk=self.kwargs.get('pk'), is_deleted=False)
        return queryset


class TaskAddView(CreateView):
    template_name = 'task/add_task.html'
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
    template_name = 'task/update_task.html'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = '/'
