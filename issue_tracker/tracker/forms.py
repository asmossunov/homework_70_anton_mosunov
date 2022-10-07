from django import forms
from django.core.exceptions import ValidationError
from tracker.models.tasks import Task
from tracker.models.types import Type
from tracker.models.statuses import Status


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        initial='New')
    types = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        initial=Type.objects.get(type_name='Task')
    )

    class Meta:
        model = Task
        fields = ('text', 'description', 'status', 'types')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 2:
            raise ValidationError('Содержание должно быть длиннее 1 символа')
        return text
