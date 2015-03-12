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
import random


def index(request):
        context_dict = {}
        categories = Category.objects.all()
	context_dict['categories'] = categories
	joke = Joke.objects.all()
        size = len(joke)
        random1 = random.randint(0, size-1)
	
        while True:
                random2 = random.randint(0, size-1)
                if random1 != random2:
                        break
                
        context_dict['joke1'] = joke[random1]
	context_dict['joke2'] = joke[random2]
	
        if request.method == 'POST':
                if '_left' in request.POST:
                        print "left"
                elif '_righ' in request.POST:
                         print "right"
                
        
	
	return render(request, 'JokeRater/index.html', context_dict)

def register_profile(request):

	completed = False
	if request.method == 'POST':
		try:
			profile = UserProfile.objects.get(user=request.user)
			profile_form = UserProfileForm(request.POST, instance=profile)
		except:
			profile_form = UserProfileForm(request.POST)
		if profile_form.is_valid():
			if request.user.is_authenticated():
				profile = profile_form.save(commit=False)
				user = request.user
				profile.user = user
				try:
					profile.picture = request.FILES['picture']
				except:
					pass
				profile.save()
				completed = True
		else:
			print profile_form.errors
		return index(request)
	else:
		profile_form = UserProfileForm(request.GET)
	return render(request, 'JokeRater/profile_registration.html', {'profile_form': profile_form, 'completed': completed})

# def about(request):
    # context_dict = {}
    # return render(request, 'JokeRater/about.html', context_dict)


# def category(request, category_name_slug):
    # context_dict = {}
    # return render(request, 'JokeRater/category.html', context_dict)


#@login_required
#def add_joke(request):
#    context_dict = {}
#    return render(request, 'JokeRater/add_joke.html', context_dict)





