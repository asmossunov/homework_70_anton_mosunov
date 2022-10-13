import re

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.db import models
from django.urls import reverse
from django.utils.deconstruct import deconstructible


class Task(models.Model):
    text = models.CharField(
        verbose_name='Текст задачи',
        max_length=200,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание задачи',
        max_length=3000,
        null=False,
        blank=True
    )

    types = models.ManyToManyField(
        to='tracker.Type',
        verbose_name='Тип',
        related_name='tasks',
        blank=True
    )
    status = models.ForeignKey(
        to='tracker.Status',
        verbose_name='Статус',
        related_name='tasks',
        on_delete=models.PROTECT
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    project = models.ForeignKey(
        verbose_name='Проект',
        to='tracker.Project',
        related_name='products',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.text} {self.description}'

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})


@deconstructible
def max_length_validator(string):
    if len(string) > 200:
        raise ValidationError("Превышена максимальная длина строки 200 символов")
    return string

@deconstructible
def first_number_validator(string):
    if re.match(r'\d', string):
        raise ValidationError('Название не должно начинаться с цифры')
    return string

@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Введённое значение "%(value) s" имеет длину %(show_value) d! ' \
              'Должно состоять не чем из %(limit_value) d символов'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)

