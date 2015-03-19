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

from datetime import date, timedelta
import random

previous = {}

def index(request):
        if request.POST.get('select') == 'left':
                jokeA = previous['joke1']
                jokeB = previous['joke2']
                if (jokeA.rating - jokeB.rating) >= 20:
                    jokeA.rating += 1
                    jokeB.rating -= 1
                elif (jokeA.rating - jokeB.rating) >= 10:
                    jokeA.rating += 2
                    jokeB.rating -= 2
                elif (jokeA.rating - jokeB.rating) >= 0:
                    jokeA.rating += 3
                    jokeB.rating -= 3
                elif (jokeA.rating - jokeB.rating) >= -10:
                    jokeA.rating += 4
                    jokeB.rating -= 4
                else:
                    jokeA.rating += 5
                    jokeB.rating -= 5
                jokeA.save()
                jokeB.save()
                print "left"
        elif request.POST.get('select') == 'right':
                jokeA = previous['joke1']
                jokeB = previous['joke2']
                if (jokeB.rating - jokeA.rating) >= 10:
                    jokeB.rating += 1
                    jokeA.rating -= 1
                elif (jokeB.rating - jokeA.rating) >= 0:
                    jokeB.rating += 2
                    jokeA.rating -= 2
                elif (jokeB.rating - jokeA.rating) >= -10:
                    jokeB.rating += 3
                    jokeA.rating -= 3
                elif (jokeB.rating - jokeA.rating) >= -20:
                    jokeB.rating += 4
                    jokeA.rating -= 4
                else:
                    jokeB.rating += 5
                    jokeA.rating -= 5
                jokeA.save()
                jokeB.save()
                print "right"
                
        context_dict = {}
        jokes = Joke.objects.order_by('-rating')
        size = len(jokes)
        random1 = random.randint(0, size-1)
        while True:
                random2 = random.randint(0, size - 1)
                if random1 != random2:
                    break
        joke1 = jokes[random1]
        joke2 = jokes[random2]
        context_dict['joke1'] = joke1
        context_dict['joke2'] = joke2
            
        for i in range(0,size):
                if jokes[i] == joke1:
                        context_dict['joke1_position'] = i+1
                elif jokes[i] == joke2:
                        context_dict['joke2_position'] = i+1
                i = i + 1

        previous['joke1'] = joke1
        previous['joke2']= joke2
        return render(request, 'JokeRater/index.html', context_dict)

def joke(request, category_name_slug):
        context_dict = {}
        JokeCategory = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = JokeCategory
        jokes = Joke.objects.filter(category=JokeCategory)
        size = len(jokes)
        try:
                p = previous['joke']
        except:
                p = -1
        while True:
                r = random.randint(0, size - 1)
                if r != p:
                    break
                
        joke = jokes[r]
        previous['joke'] = r
        context_dict['joke'] = joke

        orderedJokes = Joke.objects.all()
        orderedSize = len(orderedJokes)
        for i in range(0,orderedSize):
                if orderedJokes[i] == joke:
                        context_dict['joke_position'] = i+1
                i = i + 1
     
        return render(request, 'JokeRater/joke.html', context_dict)

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
        if request.POST.get('select') == 'left':
                jokeA = previous['joke1']
                jokeB = previous['joke2']
                if (jokeA.rating - jokeB.rating) >= 20:
                    jokeA.rating += 1
                    jokeB.rating -= 1
                elif (jokeA.rating - jokeB.rating) >= 10:
                    jokeA.rating += 2
                    jokeB.rating -= 2
                elif (jokeA.rating - jokeB.rating) >= 0:
                    jokeA.rating += 3
                    jokeB.rating -= 3
                elif (jokeA.rating - jokeB.rating) >= -10:
                    jokeA.rating += 4
                    jokeB.rating -= 4
                else:
                    jokeA.rating += 5
                    jokeB.rating -= 5
                jokeA.save()
                jokeB.save()
                print "left"
        elif request.POST.get('select') == 'right':
                jokeA = previous['joke1']
                jokeB = previous['joke2']
                if (jokeB.rating - jokeA.rating) >= 10:
                    jokeB.rating += 1
                    jokeA.rating -= 1
                elif (jokeB.rating - jokeA.rating) >= 0:
                    jokeB.rating += 2
                    jokeA.rating -= 2
                elif (jokeB.rating - jokeA.rating) >= -10:
                    jokeB.rating += 3
                    jokeA.rating -= 3
                elif (jokeB.rating - jokeA.rating) >= -20:
                    jokeB.rating += 4
                    jokeA.rating -= 4
                else:
                    jokeB.rating += 5
                    jokeA.rating -= 5
                jokeA.save()
                jokeB.save()
                print "right"
                
        context_dict = {}
        JokeCategory = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = JokeCategory
        jokes = Joke.objects.filter(category=JokeCategory)
        size = len(jokes)
        random1 = random.randint(0, size - 1)

        while True:
                random2 = random.randint(0, size - 1)
                if random1 != random2:
                        break

        joke1 = jokes[random1]
        joke2 = jokes[random2]
        context_dict['joke1'] = joke1
        context_dict['joke2'] = joke2
        orderedJokes = Joke.objects.order_by('-rating')
        orderSize = len(orderedJokes)
        for i in range(0,orderSize):
                if orderedJokes[i] == joke1:
                        context_dict['joke1_position'] = i+1
                elif orderedJokes[i] == joke2:
                        context_dict['joke2_position'] = i+1
                i = i + 1

        previous['joke1'] = joke1
        previous['joke2']= joke2
        return render(request, 'JokeRater/category.html', context_dict)
		
def overall(request):
        j = Joke.objects.order_by('-rating')[:15]
        return render(request, 'JokeRater/topOverall.html', {'overall':j})

def weekly(request):
        start_date = datetime.datetime.now().date() - timedelta(days=7)
        end_date = datetime.datetime.now().date()
        j = Joke.objects.filter(datePosted__range=(start_date, end_date)).order_by('-rating')[:15]
        return render(request, 'JokeRater/topWeekly.html', {'weekly':j})


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
