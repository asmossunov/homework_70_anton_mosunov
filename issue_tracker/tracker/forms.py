from django import forms
from django.core.exceptions import ValidationError
from tracker.models.tasks import Task
from tracker.models.types import Type
from tracker.models.statuses import Status

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
        # initial=Type.objects.get(type_name='Task')
    )

    class Meta:
        model = Task
        fields = ('text', 'description', 'status', 'types')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),

            }
