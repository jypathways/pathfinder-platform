# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from django.contrib.auth import get_user_model

from pathfinder.forms import *
from pathfinder.apps.trail.models import User, Category, Spark

class UserFormTest(TestCase):

    def setUp(self):
        pass

    def test_init(self):
        UserForm()

    def test_valid_data(self):
        form = UserForm({
            'username': 'tleela',
            'first_name': "Turanga",
            'last_name': 'Leela',
            'email': "leela@example.com",
            'password': "fn893rq_rlER",
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, "tleela")
        self.assertEqual(user.first_name, "Turanga")
        self.assertEqual(user.last_name, "Leela")
        self.assertEqual(user.email, "leela@example.com")
        self.assertEqual(user.password, "fn893rq_rlER")

    def test_blank_data(self):
        form = UserForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
            'password': ['This field is required.'],
        })

class SparkFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user('test123')
        self.category = Category.objects.create(name='Test Category')
        self.spark = Spark.objects.create(
            name='Test Spark Duplicate',
            category=self.category,
            start_date='1993-12-13',
            end_date="2014-1-1",
            url="http://test.com",
            description="This is a test description",
            author=self.user,
        )

    def test_init(self):
        AddSpark(author=self.user,)

    def test_init_without_entry(self):
        with self.assertRaises(KeyError):
            AddSpark()

    def test_valid_data(self):
        form = AddSpark({
            'name': 'Test Project',
            'category': Category.objects.filter(name="Test Category"),
            'start_date': '1993-12-13',
            'end_date': "2014-1-1",
            'url': "http://test.com",
            'description': "This is a test description",
        }, author=self.user)
        self.assertTrue(form.is_valid())
        spark = form.save()
        self.assertEqual(spark.name, "Test Project")
        self.assertEqual(spark.start_date, datetime.date(1993, 12, 13))
        self.assertEqual(spark.end_date, datetime.date(2014, 1, 1))
        self.assertEqual(spark.url, "http://test.com")
        self.assertEqual(spark.description, "This is a test description")
        self.assertEqual(spark.category, self.category)
        self.assertEqual(spark.author, self.user)

    def test_blank_data(self):
        form = AddSpark({},author=None)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'category': ['This field is required.'],
            'start_date': ['This field is required.'],
            'url': ['This field is required.'],
        })

    def test_duplicate_spark_names(self):
        form = AddSpark({
            'name': 'Test Spark Duplicate',
            'category': Category.objects.filter(name="Test Category"),
            'start_date': '1993-1-13',
            'end_date': "2014-1-12",
            'url': "http://tttt.com",
            'description': "This is a test description",
        }, author=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['Spark with this Name already exists.'],
        })
