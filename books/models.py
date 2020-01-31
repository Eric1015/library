import datetime
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_at = models.DateField(default=datetime.date(1970, 1, 1))
    genre = models.CharField(max_length=255)
    num_of_pages = models.IntegerField(default=0)