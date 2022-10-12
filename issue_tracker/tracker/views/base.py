from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from urllib.parse import urlencode

from tracker.models import Task
from tracker.forms import SearchForm

# from homework_requests import get_requests


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         get_requests()
#         tasks = Task.objects.all()
#         context = {
#             'tasks': tasks
#         }
#         return render(request, 'index.html', context)
class IndexView(ListView):
    template_name = 'index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('-created_at',)
    paginate_by = 3
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(text__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

