from django import forms
from .models import Resource, Category, Favorite 


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'description', 'author', 'link', 'Published_year')

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category 
        fields = ('cat_title',)