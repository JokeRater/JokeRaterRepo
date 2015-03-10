from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from django.shortcuts import redirect

from models import *
from forms import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import datetime


def index(request):
    context_dict = {}
<<<<<<< HEAD
    return render(request, 'JokeRater/index.html', context_dict)
=======
    return render(request,'JokeRater/index.html', context_dict)
>>>>>>> 0b5052df6f5ada83e77ea4624cd8d0089f111570


def about(request):
    context_dict = {}
    return render(request, 'JokeRater/about.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    return render(request, 'JokeRater/category.html', context_dict)


#@login_required
#def add_joke(request):
#    context_dict = {}
#    return render(request, 'JokeRater/add_joke.html', context_dict)





