from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileDetailViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.profile = Profile.objects.create(user=self.user,
                                              favorite_city='Test City')

    def test_profile_view_existing_user(self):
        response = self.client.get(reverse('profiles:profile',
                                           args=['testuser']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Test City')

    def test_profile_view_non_existing_user(self):
        response = self.client.get(reverse('profiles:profile',
                                           args=['nonexistentuser']))
        self.assertEqual(response.status_code, 200)
        # Vérifier que le template 404 est utilisé
        self.assertTemplateUsed(response, '404.html')
        # Vérifier que le message d'erreur approprié est passé au template
        self.assertContains(response, 'Profile Not Exist : Username nonexistentuser does not exist !')

    def test_index_view(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn('profiles_list', response.context)
    
    def test_profile_view_error(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "No profiles found.")