from django.db import models


class Type(models.Model):
    type_name = models.CharField(
        verbose_name='Тип',
        max_length=100
    )

    def __str__(self):
        return f'{self.type_name}'
