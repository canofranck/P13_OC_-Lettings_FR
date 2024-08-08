# tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingViewTests(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=self.address
        )

    def test_index_view(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, 'Test Letting')

    def test_letting_view(self):
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, 'Test Street')
