from django.db import models


class Status(models.Model):
    status_name = models.CharField(
        verbose_name='Статус',
        max_length=100
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.status_name}'
