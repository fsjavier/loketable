from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestModels(TestCase):
    """
    Test model
    """

    def setUp(self):
        """
        Create a test user
        """
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

    def test_first_name_populated(self):
        """
        Test first_name is automatically populated
        """
        profile = self.user.profile
        self.assertEqual(profile.first_name, 'test_user')
