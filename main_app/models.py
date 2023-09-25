from django.db import models


class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
      return f'{self.name} ({self.id})'
