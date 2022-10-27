from django.contrib import admin
from .models import Resource, Category, Favorite 

admin.site.register(Resource)
admin.site.register(Category)
admin.site.register(Favorite)

# Register your models here.
