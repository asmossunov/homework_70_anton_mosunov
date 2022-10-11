
from django.shortcuts import render

from django.views.generic import View

from tracker.models import Task

from homework_requests import get_requests


class IndexView(View):
    def get(self, request, *args, **kwargs):
        get_requests()
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)


