from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64)
    edition_year = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(datetime.now().year)],
        help_text='Format allowed: YYYY'
    )

    def __str__(self):
        return self.title
