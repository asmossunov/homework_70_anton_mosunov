from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView

from tracker.models import Task
from tracker.forms import TaskForm


class TaskView(DetailView):
    model = Task
    template_name = 'task.html'
    pk_url_kwarg = 'pk'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
    #     return context


class TaskAddView(CreateView):
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('task_detail')

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     form = TaskForm()
    #     context['form'] = form
    #     return self.render_to_response(context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         task = Task.objects.create(**form.cleaned_data)
    #         return redirect('task_detail', pk=task.pk)
    #     return render(request, 'article_create.html', context={'form': form})


