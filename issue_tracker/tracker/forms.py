from django import forms
from django.core.exceptions import ValidationError
from tracker.models.tasks import Task
from tracker.models.types import Type
from tracker.models.statuses import Status


class TaskForm(forms.ModelForm):
    # status = forms.ModelChoiceField(queryset=Status.objects.all())
    # type = forms.ModelChoiceField(queryset=Type.objects.all())

    class Meta:
        model = Task
        fields = ('text', 'description', 'status', 'type')

    def clean_title(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidationError('Должен быть длиннее 2 символов')
        return text
