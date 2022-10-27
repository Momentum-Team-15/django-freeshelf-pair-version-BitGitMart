from django.shortcuts import render, redirect, get_object_or_404
# from django.conf import settings, messages
from .forms import ResourceForm 
from .models import Resource, Category, Favorite 
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@login_required
def private_place(request):
    return HttpResponseRedirect(reverse('news:home'))

@login_required
def index(request):
    resources = Resource.objects.all() 
    categories = Category.objects.all() 
    return render(request, 'freeshelf/index.html', {'resources': resources, 'categories': categories})


def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid(): 
            resource = form.save() #may add boolean value in here
            resource.save() 
            return redirect() #we'll come back to this 
    else:
        form = ResourceForm()
    return render(request,'freeshelf/create_resource.html', {'form': form}) 

@staff_member_required
def edit_resource(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    form = ResourceForm(request.POST or None, instance=resource)
    if form.is_valid():
        resource = form.save()
        return redirect("home")
    return render(request, 'freeshelf/edit_resource.html', {'resource': resource, 'form' : form})

@staff_member_required
def delete_resource(request, resource_id):
    resource = Resource.objects.get(pk=resource_id)
    resource.delete()
    return redirect("home")

def category(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'Freeshelf/categories.html', {'category': category})

def favorite(request):
    favorited = Favorite.objects.all().order_by('-created_at')
    return render(request, 'Freeshelf/favorite.html', {'favorited': favorited} )

def add_favorite(request, resource_pk): 
    resource = get_object_or_404(Resource, pk=resource_pk)
    unfavorited = False 
    for favorite in request.user.favorites.all():
        if resource == favorite.resource:
            favorite.delete()
            unfavorited = True
    if not unfavorited:
        favorite = Favorite.objects.create(resource=resource, user=request.user)
        favorite.save()
    return redirect("home")

    


