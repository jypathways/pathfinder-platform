# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now
from django.shortcuts import render
from .forms import *


def home(request):
    today = datetime.date.today()
    return render(request, "pathfinder/index.html", {'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
    
    
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        
    return render(request, './templates/pathfinder/index.html')

def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
                
            profile.save()
            
            
            registered = True
            
        else:
            print(user_form.errors, profile_form.errors) 
            
    else:
        
        user_form = UserForm()
        profile_form = UserProfileForm()
        
        
    return render(request,
            './templatespathfinder/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
