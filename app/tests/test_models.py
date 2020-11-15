from django.contrib.auth import get_user_model
from django.test import TestCase

class TestModels(TestCase):
    def test_can_create_a_new_user(self):
        """Test a new user can be created successfully"""

        email = "test@email.com"
        password = "password123"

        user = get_user_model().create_user(
            email,
            password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        """
            Test the user email is normalized when created
            i.e user@EMAIL.cOm -> user@email.com
        """
        email = "user@EMAIL.cOm"
        user = get_user_model().create_user(email, "password123")

        self.assertEqual(user.email, email.lower())

    def test_create_new_user_with_invalid_email(self):
        """Test a new user cannot be created with an invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("invalid@email", "password123")

    def test_create_new_user_without_email(self):
        """Test a new user cannot be created without an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "password123")

    def test_create_a_new_superuser(self):
        """Test a new super user can be successfully created"""
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'password123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
