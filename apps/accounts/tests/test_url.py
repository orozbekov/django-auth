from django.urls import resolve

from rest_framework_simplejwt import views as jwt_views

from apps.accounts import views
from apps.accounts.tests.test_setup import TestSetup


class TestUrls(TestSetup):
    """Тестирование url адресы"""

    def test_register(self):
        url = self.register_url
        view_class = resolve(url).func.view_class
        return self.assertEqual(view_class, views.RegisterView)

    def test_login(self):
        url = self.login_url
        view_class = resolve(url).func.view_class
        return self.assertEqual(view_class, views.LoginView)

    def test_login_refresh(self):
        url = self.refresh_url
        view_class = resolve(url).func.view_class
        return self.assertEqual(view_class, jwt_views.TokenRefreshView)

    