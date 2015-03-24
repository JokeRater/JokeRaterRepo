from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.context_processors import csrf

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
    report = False
    
    # Try to obtain previous jokes
    try:
        jokeA = previous['joke1']
        jokeB = previous['joke2']
    except:
        jokeA = None
        jokeB = None

    # Award points to the winning joke
    # Subtract point form loosing joke
    if request.POST.get('select') == 'left':
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
    elif request.POST.get('select') == 'right':
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

    # Flags a joke if it is reported
    elif request.POST.get('select') == 'reportLeft':
        jokeA.reportFlag = True
        jokeA.save()
        report = True
    elif request.POST.get('select') == 'reportRight':
        jokeB.reportFlag = True
        jokeB.save()
        report = True


    # Get the jokes ordered by rating and the number of jokes   
    jokes = Joke.objects.order_by('-rating')
    size = len(jokes)

    # Choose a joke at random
    while True:
        random1 = random.randint(0, size - 1)
        if jokes[random1] != jokeA and jokes[random1] != jokeB:
            break
    joke1 = jokes[random1]

    # Choose another joke at random
    while True:
        random2 = random.randint(0, size - 1)
        if jokes[random2] != joke1 and jokes[random2] != jokeA and jokes[random2] != jokeB:
            break    
    joke2 = jokes[random2]

    # Pass the jokes to the template
    context_dict = {}
    context_dict['joke1'] = joke1
    context_dict['joke2'] = joke2

    # Get the rankings of the two random jokes and pass this to the template
    for i in range(0, size):
        if jokes[i] == joke1:
            context_dict['joke1_position'] = i + 1
        elif jokes[i] == joke2:
            context_dict['joke2_position'] = i + 1
        i = i + 1

    # Record the random jokes selected this time as the previous jokes
    previous['joke1'] = joke1
    previous['joke2'] = joke2
    
    context_dict['report'] = report
    context_dict.update(csrf(request))
    return render(request, 'JokeRater/index.html', context_dict)


def joke(request, category_name_slug):
    report = False
    
    # Try to obtain the previous joke
    try:
        jokeA = previous['joke']
    except:
        jokeA = None

    # Get the name of the category selected and pass it to the template
    JokeCategory = Category.objects.get(slug=category_name_slug)
    context_dict = {}
    context_dict['category'] = JokeCategory

    # Get the jokes in that category and the number there is
    jokes = Joke.objects.filter(category=JokeCategory)
    size = len(jokes)

    # Select a joke in that category at random and pass it to the template
    while True:
        random1 = random.randint(0, size - 1)
        if jokes[random1] != jokeA:
            break
    joke = jokes[random1]
    context_dict['joke'] = joke
    previous['joke'] = joke
    
    # Works out the overall ranking of the joke and passes it to the template
    orderedJokes = Joke.objects.order_by('-rating')
    orderedSize = len(orderedJokes)
    for i in range(0, orderedSize):
        if orderedJokes[i] == joke:
            context_dict['joke_position'] = i + 1
        i = i + 1

    # Flags a joke if it is reported
    if request.POST.get('select') == 'report':
        jokeA.reportFlag = True
        jokeA.save()
        report = True

    context_dict['report'] = report
    return render(request, 'JokeRater/joke.html', context_dict)

@login_required
def register_profile(request):
    completed = False
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
    return render(request, 'JokeRater/profile_registration.html',{'profile_form': profile_form, 'completed': completed})

@login_required
def profile(request):
    
    # Gets the active users details
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        return HttpResponseRedirect('/JokeRater/register_profile/')

    # Use the details from the submitted form to create a new joke
    # Otherwise pass the form to the template to the template to be renderd
    if request.method == 'POST':
        joke_form = JokeForm(request.POST)
        if joke_form.is_valid():
            joke = joke_form.save(commit="False")
            joke.postingUser = user
            joke.datePosted = datetime.datetime.now().date()
            joke.reportFlag = False
            joke_form.save(commit="True")
        else:
            print joke_form.errors
        return HttpResponseRedirect('/JokeRater/profile')
    else:
        joke_form = JokeForm()

    # Calculate the rank of all the jokes belonging to the active user
    orderedJokes = Joke.objects.order_by('-rating')
    ranks = []
    count = 1
    for joke in orderedJokes:
        if joke.postingUser == user:
            ranks.append(count)
        count = count + 1

    # Pass all the relevant details to the template
    context_dict = {}
    context_dict['user'] = user
    context_dict['profile'] = profile
    context_dict['joke_form'] = joke_form
    context_dict['uploaded_jokes'] = Joke.objects.order_by('-rating').filter(postingUser=user)
    context_dict['ranks'] = ranks
    return render(request, 'JokeRater/profile.html', context_dict)

def category(request, category_name_slug):
    report = False
    
   # Try to obtain previous jokes
    try:
        jokeA = previous['joke1']
        jokeB = previous['joke2']
    except:
        jokeA = None
        jokeB = None

    # Award points to the winning joke
    # Subtract point form loosing joke
    if request.POST.get('select') == 'left':
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
    elif request.POST.get('select') == 'right':
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
        
    # Flags a joke if it is reported
    elif request.POST.get('select') == 'reportLeft':
        jokeA.reportFlag = True
        jokeA.save()
        report = True
    elif request.POST.get('select') == 'reportRight':
        jokeB.reportFlag = True
        jokeB.save()
        report = True

    # Get the name of the category selected and pass it to the template
    JokeCategory = Category.objects.get(slug=category_name_slug)
    context_dict = {}
    context_dict['category'] = JokeCategory

    # Get all the jokes in the category
    jokes = Joke.objects.filter(category=JokeCategory)
    size = len(jokes)
    
    # Choose a joke at random
    while True:
        random1 = random.randint(0, size - 1)
        if jokes[random1] != jokeA and jokes[random1] != jokeB:
            break
    joke1 = jokes[random1]

    # Choose another joke at random
    while True:
        random2 = random.randint(0, size - 1)
        if jokes[random2] != joke1 and jokes[random2] != jokeA and jokes[random2] != jokeB:
            break    
    joke2 = jokes[random2]
    
    # Pass the jokes to the template
    context_dict['joke1'] = joke1
    context_dict['joke2'] = joke2

    # Get the rankings of the two random jokes and pass this to the template
    orderedJokes = Joke.objects.order_by('-rating')
    orderSize = len(orderedJokes)
    for i in range(0, orderSize):
        if orderedJokes[i] == joke1:
            context_dict['joke1_position'] = i + 1
        elif orderedJokes[i] == joke2:
            context_dict['joke2_position'] = i + 1
        i = i + 1

    # Record the random jokes selected this time as the previous jokes
    previous['joke1'] = joke1
    previous['joke2'] = joke2

    context_dict['report'] = report
    return render(request, 'JokeRater/category.html', context_dict)

def overall(request):
    # Get the top 15 jokes by rating
    j = Joke.objects.order_by('-rating')[:15]
    return render(request, 'JokeRater/topOverall.html', {'overall': j})


def weekly(request):
    # Get the top 15 joke by rating that were posted in the last 7 days
    start_date = datetime.datetime.now().date() - timedelta(days=7)
    end_date = datetime.datetime.now().date()
    j = Joke.objects.filter(datePosted__range=(start_date, end_date)).order_by('-rating')[:15]
    return render(request, 'JokeRater/topWeekly.html', {'weekly': j})

def suggest(request):
    search = request.POST['search']
    suggestion = ""
    suggestion_list = ["puppy dog", "cats hate dogs","raining cats and dogs"]	
    for	s in suggestion_list:
        if s.startswith(search):
            suggestion = s
    response = HttpResponse(suggestion)	
    return response

def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    jokes = Joke.objects.filter(content__contains=search_text)

    return render(request, 'JokeRater/ajax_search.html', {'jokes':jokes})
