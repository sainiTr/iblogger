from django.db import models

from tinymce.models import HTMLField

# Create your models here.

# Create your models here.

class Digitalpage(models.Model):
    name = models.CharField(max_length=200)
    page = models.TextField()

    def __str__(self) -> str:
        return self.name 