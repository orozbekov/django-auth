from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetup(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.refresh_url = reverse('token-refresh')

        self.user_register = {
            'username': 'tima',
            'email': 'tima@gmail.com',
            'password': 'qwertyuiop123!',
            'confirm_password': 'qwertyuiop123!',
        }

        self.user_login = {
            'username': 'tima',
            'password': 'qwertyuiop123!'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
