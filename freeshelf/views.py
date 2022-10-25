from django.shortcuts import render, redirect
# from django.conf import settings, messages
from .forms import ResourceForm
from .models import Resource
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponseRedirect
from django.urls import reverse 


# Create your views here.
@login_required
def private_place(request):
    return HttpResponseRedirect(reverse('news:home'))

@login_required
def index(request):
    resources = Resource.objects.all() 
    return render(request, 'freeshelf/index.html', {'resources': resources})


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