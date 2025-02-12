from django.db import models
from shared.models import BaseModel


# Create your models here.
class Book(BaseModel):
    title = models.CharField(max_length=255, verbose_name="title")
    content = models.CharField(max_length=255, verbose_name="content")
    body = models.TextField(verbose_name="body")
    author = models.CharField(max_length=200, verbose_name="author")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="isbn")
    price = models.DecimalField(max_digits=16, decimal_places=2, verbose_name="price")


    def __str__(self):
        return f"{self.title} --> {self.author}"