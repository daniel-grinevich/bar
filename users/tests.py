from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="james",
            email="james@gmail.com",
            password="testpass123",
        )

        self.assertEqual(user.username, "james")
        self.assertEqual(user.email, "james@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="superjames", email="superjames@gmail.com", password="supertest123"
        )
        self.assertEqual(user.username, "superjames")
        self.assertEqual(user.email, "superjames@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
