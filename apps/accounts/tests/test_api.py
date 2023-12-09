from rest_framework.test import APITestCase
from apps.accounts.tests.test_setup import TestSetup
from apps.accounts.models import User


class TestSetup(TestSetup):

    def test_user_registration_with_correct_data(self):
        response = self.client.post(self.register_url, self.user_register, format='json')
        self.assertEqual(response.status_code, 201)

    def test_user_registration_with_invalid_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 400)

    def test_user_login_and_refresh(self):
        self.client.post(self.register_url, self.user_register, format='json')
        response = self.client.post(self.login_url, self.user_login, format='json')
        self.assertEqual(response.status_code, 200)
        tokens = response.data['tokens']
        self.assertIn('refresh', tokens)
        self.assertIn('access', tokens)

        refresh = {
            'refresh': tokens.get('refresh')
        }

        result = self.client.post(self.refresh_url, refresh)
        self.assertEqual(result.status_code, 200)
        self.assertIn('access', result.data)

    def test_user_login_with_invalid_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, 400)