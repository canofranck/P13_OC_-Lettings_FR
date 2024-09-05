from django.test import TestCase, override_settings, Client
from django.urls import reverse
from unittest.mock import patch


class IndexViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class Error500ViewTests(TestCase):

    @override_settings(DEBUG=False)
    @patch('oc_lettings_site.views.sentry_log')
    def test_error500_view(self, mock_sentry_log):
        client = Client()
        response = client.get('/check_500/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '500.html')
        mock_sentry_log.assert_called_once_with(error_type="error",
                                                error_message="500 error")