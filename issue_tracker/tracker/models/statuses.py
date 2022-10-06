from django.db import models


class Status(models.Model):
    status_name = models.CharField(
        verbose_name='Статус',
        max_length=100
    )

    def __str__(self):
        return f'{self.status_name}'
