# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse

class TestRegistrationPage(TestCase):
    
    def test_uses_register_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "../templates/trail/register.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "base.html")
