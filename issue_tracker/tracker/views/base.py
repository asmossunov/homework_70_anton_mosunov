
from django.shortcuts import render

from django.views.generic import View

from tracker.models import Task


class IndexView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)
