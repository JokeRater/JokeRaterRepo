from django.test import TestCase
from JokeRaterApp.models import Joke


class JokeRaterTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("TestUser", "testemail@example.com", "testpassword")

        Joke.objects.create(category=doctor, content="Doctor, Doctor my son has swallowed my pen, what should I do?",
                            punchline="Use a pen 'til I get there.", rating="6", postingUser=tesUser,
                            datePosted=datetime.datetime.now().date())

    def test_content(self):
        user = User.objects.get(name="TestUser")
        joke = Joke.objects.get(punchline="Use a pen 'til I get there.")

        self.assertEqual(user.email, "testemail@example.com")
        self.assertEqual(joke.rating, "6")
		
		
