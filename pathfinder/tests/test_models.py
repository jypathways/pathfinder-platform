from django.test import TestCase

from pathfinder.apps.trail.models import *


class UserModelTest(TestCase):

    def test_string_representation(self):
        user = User(username="test123")
        user_profile = UserProfile(user=user)
        self.assertEqual(str(user_profile), user_profile.user.username)

class CategoryModelTest(TestCase):

    def test_string_representation(self):
        category = Category(name="Test Category")
        self.assertEqual(str(category), category.name)

class SparkModelTest(TestCase):

    def test_string_representation(self):
        spark = Spark(name="Test Spark")
        self.assertEqual(str(spark), spark.name)
