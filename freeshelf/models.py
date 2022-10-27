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
    Created_at = models.DateTimeField(auto_now_add=True)
    Published_year = models.IntegerField()
    category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.CASCADE, related_name="resources")


    def publish(self):
        self.save() 

    def __str__(self):
        new_line = '\n'
        return f"{self.title} by {self.author}{new_line}Year published: {self.Published_year}{new_line}{self.description}"


class Category(models.Model):
    cat_title = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.cat_title}"

class Favorite(models.Model):
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, related_name='favorites', null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name='favorites')
    Created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    

    