# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):

    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "trail/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")

class TestRegistrationPage(TestCase):

    def test_uses_register_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "../templates/trail/register.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(response, "base.html")

# class TestSparkCreationPage(TestCase):
#
#     def test_uses_add_spark_template(self):
#         response = self.client.get(reverse("add_spark"))
#         self.assertTemplateUsed(response, "../templates/trail/addSpark.html")
#
#     def test_uses_base_template(self):
#         response = self.client.get(reverse("add_spark"))
#         self.assertTemplateUsed(response, "base.html")
