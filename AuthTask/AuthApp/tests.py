from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LoginFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='demo', password='demo1234')

    def test_failed_login_shows_error_message(self):
        response = self.client.post(
            reverse('user_login'),
            {'username': 'demo', 'password': 'wrong-password'},
            follow=True,
        )

        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'Invalid Username or Password. Try Again.')

    def test_successful_login_shows_welcome_message(self):
        response = self.client.post(
            reverse('user_login'),
            {'username': 'demo', 'password': 'demo1234'},
            follow=True,
        )

        self.assertRedirects(response, reverse('about'))
        self.assertContains(response, 'Welcome demo')
