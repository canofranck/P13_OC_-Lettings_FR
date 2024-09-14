from django.test import TestCase
from lettings.models import Address
from lettings.models import Letting


class AddressModelTests(TestCase):

    def test_address_str(self):
        # Création d'une instance d'Address
        address = Address(number="6", street="avenue de la republique")

        # Vérifie que la méthode __str__ retourne la bonne représentation
        self.assertEqual(str(address), "6 avenue de la republique")


class LettingModelTests(TestCase):

    def test_letting_str(self):
        # Création d'une instance de Letting
        letting = Letting(title="Test instance Letting")

        # Vérifie que la méthode __str__ retourne la bonne représentation
        self.assertEqual(str(letting), "Test instance Letting")
