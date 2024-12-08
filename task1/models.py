from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()

    def __str__(self):
        return self.title



class Author(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.name