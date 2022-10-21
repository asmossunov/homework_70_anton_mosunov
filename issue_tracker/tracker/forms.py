from django import forms
from tracker.models.tasks import Task
from tracker.models.types import Type
from tracker.models.statuses import Status
from tracker.models.projects import Project

from tracker.models.tasks import MinLengthValidator

from tracker.models.tasks import max_length_validator, first_number_validator


class TaskForm(forms.ModelForm):
    text = forms.CharField(
        label='Текст',
        validators=(MinLengthValidator(5), max_length_validator, first_number_validator, )
    )
    status = forms.ModelChoiceField(
        label='Статус',
        queryset=Status.objects.all(),
        initial='New'
    )
    types = forms.ModelMultipleChoiceField(
        label='Тип',
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ('text', 'description', 'status', 'types')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(
        label='Название проекта',
        validators=(MinLengthValidator(5), max_length_validator, first_number_validator, )
    )
    project_description = forms.CharField(
        label='Описание',
        widget=forms.Textarea
    )
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget)

    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'start_date', 'end_date')
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-input'}),
            'projects_description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')
