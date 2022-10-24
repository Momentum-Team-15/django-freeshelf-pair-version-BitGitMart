from django.shortcuts import render, redirect
from django.conf import settings, messages
from django.db import transaction 
from django.contrib.auth.decorators import login_required 
from django.utils.translation import ugettext_lazy as _
from .forms import UserForm, ProfileForm 

@login_required
@transaction.atomic 

def update_profile(request): 
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid(): 
            user_form.save()
            profile_form.save() 
            messages.success(request, _('You are a special updater'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('You make many errors.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form, 
        'profile_form': profile_form
    }) 




# Create your views here.
