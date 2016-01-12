# -*- coding: utf-8 -*-
import datetime
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView
from .apps.trail.models import *
import json


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

def spark_details(request, slug):
    spark = get_object_or_404(Spark, slug=slug)
    return render(request, 'trail/spark.html', {'spark': spark})
    
@login_required
def add_spark(request):
    if request.method == 'POST':
        form = AddSpark(request.POST)

        if form.is_valid():
            spark = form.save()
            spark.author = request.user
            spark.save()
            return render(request, 'trail/spark.html', {'spark': spark})
    else:
        form = AddSpark()

    return render(request, 'trail/addSpark.html', {
        'form': form,
    })
    
@login_required
def get_path(request):
    author_id = request.user.id
    return render(request, 'trail/myPath.html', {'json_file': contruct_json(author_id)})

def contruct_json(author_id):
    sparks = Spark.objects.filter(author=author_id)
    json_file = {}
    json_file['events'] = populate_events(sparks)
    return json.dumps(json_file)

def populate_events(sparks):
    events = []
    for spark in sparks:
        dict = {}
        if spark.url is not None:
            dict['media'] = format_media(spark.url)
        if spark.start_date is not None:
            dict['start_date'] = format_date(spark.start_date)
        if spark.end_date is not None:
            dict['end_date'] = format_date(spark.end_date)
        if spark.description is not None:
            dict['text'] = format_text(spark.name, spark.description)
        events.append(dict)
    return events

def format_media(url):
    dict = {}
    dict['url'] = url
    return dict

def format_date(date):
    dict = {}
    dict['month'] = date.month
    dict['day'] = date.day
    dict['year'] = date.year
    return dict

def format_text(name, description):
    dict = {}
    dict['headline'] = name
    dict['text'] = description
    return dict
 

    