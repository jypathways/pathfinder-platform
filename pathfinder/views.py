# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .apps.trail.models import *


def home(request):
    today = datetime.date.today()
    return render(request, "trail/index.html", {'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
    
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'trail/login.html', {})
        
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
              
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            # profile = profile_form.save(commit=False)
            # profile.user = user
            
            # if 'picture' in request.FILES:
            #     profile.picture = request.FILES['picture']
 
            # profile.save()

            registered = True
            
        else:
            # print(user_form.errors, profile_form.errors) 
            print(user_form.errors)      
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()    
    return render(request,
            '../templates/trail/register.html',
            {'user_form': user_form, 'registered': registered} )

def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'trail/project.html', {'project': project})