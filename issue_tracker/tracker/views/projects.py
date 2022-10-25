from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView

from tracker.models import Project, Task
from tracker.forms import ProjectForm

from tracker.forms import AddUserForm


class GroupPermission(UserPassesTestMixin):
    groups = []
    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectView(DetailView):
    template_name = 'project/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at').exclude(is_deleted=True)
        context['tasks'] = tasks
        return context


class ProjectCreateView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
    model = Project
    groups = ['Project Manager']

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project.objects.create(**form.cleaned_data)
            project.users.add(request.user)
            return redirect('project_detail', pk=project.pk)

        return render(request, 'project/project_create.html', context={'form': form})


class ProjectUpdateView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'
    groups = ['Project Manager']


class ProjectDeleteView(GroupPermission, LoginRequiredMixin, DeleteView):
    template_name = 'project/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
    groups = ['Project Manager']


class ProjectAddUserView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, TemplateView):
    template_name = 'project/project_add_user.html'
    model = Project
    groups = ['Project Manager', 'Team Lead']


    def post(self, request, *args, **kwargs):
        self.form = AddUserForm(self.request.POST)
        self.user_form_value = self.get_users()
        if self.user_form_value:
            project_id = self.kwargs.get('pk')
            project = Project.objects.get(id=project_id)
            users = self.user_form_value
            for user in users:
                user = User.objects.get(username=user.username)
                project.users.add(User.objects.get(username=user.username))
            return redirect('project_detail', pk=project_id)

    def dispatch(self, request, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs.get('pk'))
        if request.user != 'root':
            return super().dispatch(request, *args, **kwargs)
        else:
            if request.user not in project.users.all():
                raise PermissionDenied


    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('users')
        return None

    def get_users(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('users')
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectAddUserView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = AddUserForm
        return context


class ProjectUserUpdateView(GroupPermission, LoginRequiredMixin, UpdateView):
    model = Project
    form_class = AddUserForm
    template_name = 'project/project_add_user.html'
    groups = ['Project Manager', 'Team Lead']
