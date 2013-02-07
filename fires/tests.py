"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

class FireViewTest(TestCase):

    def test_status_code_all_data(self):
        response = self.client.get(reverse('firedata'))
        self.assertEqual(200, response.status_code)
