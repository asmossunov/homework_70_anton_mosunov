from django.db import models
from django.urls import reverse


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
    type = models.ForeignKey(
        to='tracker.Type',
        verbose_name='Тип',
        related_name='tasks',
        on_delete=models.RESTRICT
    )
    status = models.ForeignKey(
        to='tracker.Status',
        verbose_name='Статус',
        related_name='tasks',
        on_delete=models.RESTRICT
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
