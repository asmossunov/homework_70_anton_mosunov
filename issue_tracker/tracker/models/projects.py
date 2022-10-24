from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Project(models.Model):
    start_date = models.DateField(
        verbose_name='Дата начала',
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
        null=False,
        blank=True,
        default=None
    )
    project_name = models.CharField(
        verbose_name='Название проекта',
        max_length=200,
        null=False,
        blank=False
    )
    project_description = models.TextField(
        verbose_name='Текст',
        max_length=3000,
        null=False,
        blank=False
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    users = models.ManyToManyField(
        User,
        verbose_name='Пользователь',
        related_name='projects'
    )

    def __str__(self):
        return f"{self.project_name} - {self.project_description}"

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
