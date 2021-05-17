from django.test import TestCase, Client 
from .recommendation import genre_recommendations
from .models import *
from .views import *
from django.urls import reverse,resolve
from django.contrib.auth.models import User
class TestModel(TestCase): 
    def test_user(self):
        user = User.objects.create_user(username="username", password="password1", email="email@gmail.com", first_name="first_name", last_name="last_name")
        user.save()
        profile1 = UserProfile.objects.create(id=user.id,user = user,age=18,address="handigau")
        self.assertEqual(profile1.age,18)
        self.assertEqual(profile1.address,"handigau")

class TestURLS(TestCase):
    def test_list_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url).func,user_login)

class TestRecommendation(TestCase):
    def test_recommendation(self):
        test = genre_recommendations("naruto")

        self.assertIsNotNone(test)

class TestComment(TestCase):
    def test_comment(self):
        msg = "TEsting@=&&`"
        comment.objects.create(message=msg)
        test = comment.objects.get(message=msg)
        #self.assertIsNotNone(test)
        self.assertEqual(msg, test.message)

                