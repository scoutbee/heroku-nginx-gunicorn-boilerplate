from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from wueww.counter.models import Counter


class DishApiTests(TestCase):
    """Test the dish api"""

    def setUp(self):
        self.client = APIClient()

    def test_get_initial_counter(self):

        url = reverse('counter:get-counter')

        res = self.client.get(url)
        counter = Counter.objects.first()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            "value": counter.value
        })

    def test_increase_initial_counter(self):

        url = reverse('counter:increase-counter')

        res = self.client.post(url)
        counter = Counter.objects.first()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            "value": counter.value
        })

        url = reverse('counter:get-counter')

        res = self.client.get(url)
        counter = Counter.objects.first()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            "value": counter.value
        })
