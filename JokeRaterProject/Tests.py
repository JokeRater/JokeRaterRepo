from django.test import TestCase
from JokeRaterApp.models import Joke, Category
from django.contrib.auth.models import User
from datetime import date, timedelta
import datetime


class JokeRaterTestCase(TestCase):
    def setUp(self):

        #setup is also a test to evaluate creating and populating users, categories and jokes
        user = User.objects.create_user("testUser", "testemail@example.com", "testpassword")
        user.save

        doctor = Category(name="Doctor-Doctor")
        pun = Category(name="Puns")
        doctor.save()
        pun.save()

        joke1 = Joke(category=doctor, content="Patient: Doctor, Doctor my son swallowed a pen!",
                     punchline="Doctor: Use a pencil til I get there.", rating="6", postingUser=user,
                     datePosted=datetime.datetime.now().date())
        joke2 = Joke(category=pun, content="Did you hear about the guy who's left side was cut off?",
                     punchline="He's all right now.", rating="3", postingUser=user,
                     datePosted=datetime.date(2014, 8, 4))
        joke1.save()
        joke2.save()


    def test_content(self):
        # get
        user = User.objects.get(username="testUser")
        doctor = Category.objects.get(name="Doctor-Doctor")
        pun = Category.objects.get(name="Puns")
        jokeA = Joke.objects.get(punchline="Doctor: Use a pencil til I get there.")
        jokeB = Joke.objects.get(punchline="He's all right now.")

        # assert user attributes
        self.assertEqual(user.username, "testUser")
        self.assertEqual(user.email, "testemail@example.com")
        # testpassword is encoded

        # assert category
        self.assertEqual(doctor.name, "Doctor-Doctor")
        self.assertEqual(pun.name, "Puns")

        # assert joke attributes
        self.assertEqual(jokeA.punchline, "Doctor: Use a pencil til I get there.")
        self.assertEqual(jokeA.rating, 6)
        self.assertEqual(jokeB.content, "Did you hear about the guy who's left side was cut off?")
        self.assertEqual(jokeA.datePosted, datetime.datetime.now().date())
        self.assertEqual(jokeB.datePosted, datetime.date(2014, 8, 4))
        #assert postingUser object
        self.assertEqual(jokeA.postingUser, user)
        self.assertEqual(jokeB.postingUser, user)
        #assert categories
        self.assertEqual(jokeA.category, doctor)
        self.assertEqual(jokeB.category, pun)