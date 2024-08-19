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
        self.assertIn('lettings_list', response.context)

    def test_letting_view(self):
        response = self.client.get(
            reverse('lettings:letting', args=[self.letting.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Test Letting')
        self.assertContains(response, 'Test Street')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(response.context['address'], self.letting.address)

    def test_letting_view_not_found(self):
        response = self.client.get(reverse('lettings:letting', args=[999]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, "Letting id n°999 does not exist !")

    def test_letting_view_value_error(self):
        response = self.client.get(reverse('lettings:letting',
                                           args=['invalid_id']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, "ValueError : an number is requires but"
                            + " got : invalid_id")
