from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="testuser",
            password="testpass123",
            email="test@example.com",
            role="developer",
            contact_number="1234567890",
            address="123 Main St",
        )

    def test_user_content(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.role, "developer")
        self.assertEqual(user.contact_number, "1234567890")
        self.assertEqual(user.address, "123 Main St")
