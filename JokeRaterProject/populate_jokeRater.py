import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JokeRaterProject.settings')

import django
django.setup()

from JokeRaterApp.models import Category, Joke, UserProfile
from django.contrib.auth.models import User
from datetime import date, timedelta
import datetime
import random


def populate():
    pun = Category(name="Puns")
    pun.save()
    doctor = Category(name="Doctor-Doctor")
    doctor.save()
    play = Category(name="Play-on-Words")
    play.save()
    science = Category(name="Science")
    science.save()

    chris = User.objects.create_user( "Chris", "chrisbrown365@btinternet.com", "chris" )
    chris.first_name="Chris"
    chris.is_superuser=True
    chris.is_staff=True
    chris.date_joined=datetime.datetime.today()
    chris.last_login=datetime.datetime.today()
    chris.save
    chrisProfile = UserProfile(user=chris,location="Glasgow")
    chrisProfile.save



    bob = User.objects.create_user( "Bob", "bob@gmail.com", "bob" )
    bob.first_name="bob"
    bob.is_superuser=True
    bob.is_staff=True
    bob.date_joined=datetime.datetime.today()
    bob.last_login=datetime.datetime.today()
    bob.save
    bobProfile = UserProfile(user=bob,location="London")
    bobProfile.save

    Tim = User.objects.create_user( "Tim", "tim@gmail.com", "tim" )
    Tim.first_name="tim"
    Tim.is_superuser=True
    Tim.is_staff=True
    Tim.date_joined=datetime.datetime.today()
    Tim.last_login=datetime.datetime.today()
    Tim.save
    TimProfile = UserProfile(user=Tim,location="Birmingham")
    TimProfile.save

    test = User.objects.create_user( "test", "a@b.com", "test" )
    test.first_name="test"
    test.is_superuser=True
    test.is_staff=True
    test.date_joined=datetime.datetime.today()
    test.last_login=datetime.datetime.today()
    test.save
    testProfile = UserProfile(user=test,location="a place")
    testProfile.save



    joke = Joke(category=doctor,content="Patient: Doctor, Doctor I feel like a pair of curtains",punchline="Doctor: Pull yourself together",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor I think I'm a bell?",punchline="Doctor: Take these and if it doesn't help give me a ring! ",rating=random.randint(-20, 20),postingUser=chris,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor I think I'm suffering from Deja Vu!",punchline="Doctor: Didn't I see you yesterday? ",rating=random.randint(-20, 20),postingUser=Tim,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=doctor,content="Patient: Doctor, Doctor, how do I stop my nose from running?!",punchline="Doctor: Stick your foot out and trip it up! ",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=play,content="What happens to a frog's car when it breaks down?",punchline="It gets toad away. ",rating=random.randint(-20, 20),postingUser=Tim,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=play,content="Why was six scared of seven? ",punchline="Because seven ate nine. ",rating=random.randint(-20, 20),postingUser=chris,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=play,content="What is the difference between snowmen and snowwomen",punchline="Snowballs. ",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=play,content="What do you call a bear with no teeth?",punchline="A gummy bear. ",rating=random.randint(-20, 20),postingUser=Tim,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=play,content="I never wanted to believe that my Dad was stealing from his job as a road worker.",punchline="But when I got home, all the signs were there. ",rating=random.randint(-20, 20),postingUser=chris,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=pun,content="I wondered why the baseball was getting bigger.",punchline="Then it hit me.",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=pun,content="I couldn't quite remember how to throw a boomerang,",punchline="but eventually it came back to me.",rating=random.randint(-20, 20),postingUser=Tim,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=pun,content="Police were called to a daycare.",punchline="A three-year-old was resisting a rest.",rating=random.randint(-20, 20),postingUser=chris,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=pun,content="Don't trust people that do acupuncture",punchline="they're back stabbers.",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=pun,content="I used to have a fear of hurdles,",punchline="but I got over it.",rating=random.randint(-20, 20),postingUser=Tim,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=science,content="Anyone know any jokes about sodium? ",punchline="Na",rating=random.randint(-20, 20),postingUser=chris,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=science,content="I would tell you a chemistry joke...",punchline="...but all the good ones are gone",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=science,content="What do you call a clown who's in jail? ",punchline="A silicon",rating=random.randint(-20, 20),postingUser=Tim,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=science,content="Did you hear about the man who got cooled to absolute zero?",punchline="He's 0K now",rating=random.randint(-20, 20),postingUser=chris,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()
    joke = Joke(category=science,content="Why did the acid go to the gym?",punchline="To become a buffer solution",rating=random.randint(-20, 20),postingUser=bob,datePosted=datetime.datetime.now().date()- timedelta(days=random.randint(0, 10)),reportFlag=False)
    joke.save()

# Start execution here!
if __name__ == '__main__':
    print "Starting Joke Rater population script..."
    populate()
