from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'
