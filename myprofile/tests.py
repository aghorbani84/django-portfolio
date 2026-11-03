from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, Project


class PortfolioTests(TestCase):
    def test_homepage_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ابوالفضل قربانی")

    def test_contact_form_saves_message(self):
        response = self.client.post(reverse("home"), {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Hello",
            "message": "A test message with enough content.",
        })
        self.assertRedirects(response, reverse("home"))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_project_is_visible(self):
        Project.objects.create(title="Sample", summary="Sample project")
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Sample")

    def test_signup_creates_account(self):
        response = self.client.post(reverse("signup"), {
            "username": "newuser",
            "email": "new@example.com",
            "password1": "A-strong-password-2026!",
            "password2": "A-strong-password-2026!",
        })
        self.assertRedirects(response, reverse("home"))
        self.assertTrue(get_user_model().objects.filter(username="newuser").exists())
