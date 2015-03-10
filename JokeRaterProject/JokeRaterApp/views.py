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
    return render(request,'JokeRater/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'JokeRater/about.html', context_dict)
	
def category(request, category_name_slug):
    context_dict = {}
    return render(request, 'JokeRater/category.html', context_dict)
	
@login_required
def add_category(request):
    context_dict = {}
    return render(request, 'rango/add_category.html', context_dict)





