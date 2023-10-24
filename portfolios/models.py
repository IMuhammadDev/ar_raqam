from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_completed = models.DateField()
    categories = models.ManyToManyField(Category)
