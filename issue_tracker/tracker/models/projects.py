from django.db import models


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

