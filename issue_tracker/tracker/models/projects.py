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
