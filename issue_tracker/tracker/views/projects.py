from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from tracker.models import Project, Task
from tracker.forms import ProjectForm


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectView(DetailView):
    template_name = 'project_detail.html'
    model = Project



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at').exclude(is_deleted=True)
        context['tasks'] = tasks
        return context


class ProjectCreateView(SuccessDetailUrlMixin, CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Project


class ProjectUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'project_update.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'


class ProjectDeleteView(DeleteView):
    template_name = 'project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
