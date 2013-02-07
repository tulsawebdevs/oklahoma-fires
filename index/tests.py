"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class IndexTest(TestCase):
    def test_index_page(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
