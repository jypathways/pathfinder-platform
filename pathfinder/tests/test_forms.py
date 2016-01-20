# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth import get_user_model

from pathfinder.forms import *
from pathfinder.apps.trail.models import User

class UserFormTest(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user('test123')

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
