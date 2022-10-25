# from django.conf import settings 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass

class Resource(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    description = models.TextField() 
    link = models.URLField(max_length=200)
    Created_at = models.DateTimeField(default=timezone.now)
    Published_year = models.IntegerField()

    def publish(self):
        self.save() 

    def __str__(self):
        new_line = '\n'
        return f"{self.title} by {self.author}{new_line}Year published: {self.Published_year}{new_line}{self.description}"
