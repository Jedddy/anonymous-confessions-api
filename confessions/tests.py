from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Confession

class ConfessionTests(APITestCase):
    def test_create_confession(self):
        """Ensure we can create a new confession object."""

        url = reverse('confession-list')
        data = {'title': 'test', 'confession': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Confession.objects.count(), 1)
        self.assertEqual(Confession.objects.get().title, 'test')

    def test_get_confession(self):
        """Get 1 confession"""

        url_post = reverse('confession-list')
        data_post = {'title': 'test', 'confession': 'test'}
        self.client.post(url_post, data_post, format='json')

        url = reverse('confession-detail', kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test')
