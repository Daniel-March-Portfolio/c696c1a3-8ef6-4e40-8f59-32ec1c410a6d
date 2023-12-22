from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(50)])

    def __str__(self):
        return self.name
