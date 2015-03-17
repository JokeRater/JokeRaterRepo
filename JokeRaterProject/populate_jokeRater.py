import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JokeRaterProject.settings')

import django
django.setup()

from JokeRaterApp.models import Category, Joke
from django.contrib.auth.models import User


def populate():
    pun = Category(name="Puns")
    pun.save()
    doctor = Category(name="Doctor-Doctor")
    doctor.save()
    play = Category(name="Play-on-Words")
    play.save()

    chris = User(username="Chris",email="chrisbrown365@btinternet.com",password="chris")
    chris.save
    
	
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor I feel like a pair of curtains",punchline="Doctor: Pull yourself together",rating="6",postingUser=chris)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor people keep ignoring me",punchline="Doctor: Next please",rating="10",postingUser=chris)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor I think I'm a bell?",punchline="Doctor: Take these and if it doesn't help give me a ring! ",rating="9",postingUser=chris)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor I think I'm suffering from Deja Vu!",punchline="Doctor: Didn't I see you yesterday? ",rating="4",postingUser=chris)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor, how do I stop my nose from running?!",punchline="Doctor: Stick your foot out and trip it up! ",rating="12",postingUser=chris)
    joke.save()
    joke = Joke(category=play,content="What happens to a frog's car when it breaks down?",punchline="It gets toad away. ",rating="5",postingUser=chris)
    joke.save()
    joke = Joke(category=play,content="Why was six scared of seven? ",punchline="Because seven ate nine. ",rating="15",postingUser=chris)
    joke.save()
    joke = Joke(category=play,content="What is the difference between snowmen and snowwomen",punchline="Snowballs. ",rating="0",postingUser=chris)
    joke.save()
    joke = Joke(category=play,content="What do you call a bear with no teeth?",punchline="A gummy bear. ",rating="10",postingUser=chris)
    joke.save()
    joke = Joke(category=play,content="I never wanted to believe that my Dad was stealing from his job as a road worker.",punchline="But when I got home, all the signs were there. ",rating="9",postingUser=chris)
    joke.save()
	

##    add_page(cat=python_cat,
##        title="Official Python Tutorial",
##        url="http://docs.python.org/2/tutorial/",
##        views=100,)
##
##    add_page(cat=python_cat,
##        title="How to Think like a Computer Scientist",
##        url="http://www.greenteapress.com/thinkpython/",
##        views=2,)
##
##    add_page(cat=python_cat,
##        title="Learn Python in 10 Minutes",
##        url="http://www.korokithakis.net/tutorials/python/",
##        views=99,)
##
##    django_cat = add_cat("Django",64,32)
##
##    add_page(cat=django_cat,
##        title="Official Django Tutorial",
##        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
##        views=36)
##
##    add_page(cat=django_cat,
##        title="Django Rocks",
##        url="http://www.djangorocks.com/",
##        views=95)
##
##    add_page(cat=django_cat,
##        title="How to Tango with Django",
##        url="http://www.tangowithdjango.com/",
##        views=4)
##
##    frame_cat = add_cat("Other Frameworks",32,16)
##
##    add_page(cat=frame_cat,
##        title="Bottle",
##        url="http://bottlepy.org/docs/dev/",
##        views=79)
##
##    add_page(cat=frame_cat,
##        title="Flask",
##        url="http://flask.pocoo.org",
##        views=23)
##
##    student_cat = add_cat("Chris Brown - 2077762b")
##
##    add_page(cat=student_cat,
##             title="Github",
##             url="https://github.com/2077762b",
##             views=27)
##
##    add_page(cat=student_cat,
##             title="PythonAnywhere",
##             url="https://www.pythonanywhere.com/user/2077762b/consoles/",
##            views=19)
##
##    # Print out what we have added to the user.
##    for c in Category.objects.all():
##        for p in Page.objects.filter(category=c):
##            print "- {0} - {1}".format(str(c), str(p))
##
##def add_page(cat, title, url, views):
##    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
##    return p
##
##def add_cat(name, views=0, likes=0):
##    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
##    return c
##
    
# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
