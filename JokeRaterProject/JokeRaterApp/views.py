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
    joke = Joke.objects.all()
    size = len(joke)
    random1 = random.randint(0, size - 1)

    while True:
        random2 = random.randint(0, size - 1)
        if random1 != random2:
            break

    joke1 = joke[random1]
    joke2 = joke[random2]
    context_dict['joke1'] = joke1
    context_dict['joke2'] = joke2

    if request.POST.get('select') == 'left':
        print joke1.rating
        print joke2.rating
        if (joke1.rating - joke2.rating) >= 20:
            joke1.rating += 1
            joke2.rating -= 1
        elif (joke1.rating - joke2.rating) >= 10:
            joke1.rating += 2
            joke2.rating -= 2
        elif (joke1.rating - joke2.rating) >= 0:
            joke1.rating += 3
            joke2.rating -= 3
        elif (joke1.rating - joke2.rating) >= -10:
            joke1.rating += 4
            joke2.rating -= 4
        else:
            joke1.rating += 5
            joke2.rating -= 5
        joke1.save()
        joke2.save()
        print "left"
        print joke1.rating
        print joke2.rating

    elif request.POST.get('select') == 'right':
        print joke1.rating
        print joke2.rating
        if (joke2.rating - joke1.rating) >= 20:
            joke2.rating += 1
            joke1.rating -= 1
        elif (joke2.rating - joke1.rating) >= 10:
            joke2.rating += 2
            joke1.rating -= 2
        elif (joke2.rating - joke1.rating) >= 0:
            joke2.rating += 3
            joke1.rating -= 3
        elif (joke2.rating - joke1.rating) >= -10:
            joke2.rating += 4
            joke1.rating -= 4
        else:
            joke2.rating += 5
            joke1.rating -= 5
        joke1.save()
        joke2.save()
        print "right"
        print joke1.rating
        print joke2.rating

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
    return render(request, 'JokeRater/profile_registration.html',
                  {'profile_form': profile_form, 'completed': completed})


@login_required
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context_dict = {}
    completed = False

    if request.method == 'POST':
        joke_form = JokeForm(request.POST)
        if joke_form.is_valid():
            joke = joke_form.save(commit=False)
            joke.rating = 0
            category = Category.objects.all()
            category = category[0]
            joke.category = category
            joke.save()
            completed = True
        else:
            print joke_form.errors
    else:
        joke_form = JokeForm(request.GET)

    context_dict['user'] = user
    context_dict['profile'] = profile
    context_dict['joke_form'] = joke_form
    context_dict['completed'] = completed
    return render(request, 'JokeRater/profile.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    if request.method == 'POST':

        try:
            query = request.POST['query'].strip()

            if query:
                result_list = run_query(query)

                context_dict['result_list'] = result_list
                context_dict['query'] = query
        except:
            pass

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        jokes = Joke.objects.filter(category=category).order_by('-rating')
        context_dict['pages'] = jokes
        context_dict['category'] = category
        if not context_dict['query']:
            context_dict['query'] = category.name
    except Category.DoesNotExist:
        return render(request, 'JokeRater/category.html', context_dict)

    if not context_dict['query']:
        context_dict['query'] = category.name

    return render(request, 'JokeRater/category.html', context_dict)

# def about(request):
# context_dict = {}
# return render(request, 'JokeRater/about.html', context_dict)


# def category(request, category_name_slug):
# context_dict = {}
# return render(request, 'JokeRater/category.html', context_dict)


# @login_required
#def add_joke(request):
#    context_dict = {}
#    return render(request, 'JokeRater/add_joke.html', context_dict)





