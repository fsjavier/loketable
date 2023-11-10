from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product


class TestModels(TestCase):
    """
    Test model
    """

    def setUp(self):
        """
        Create a test user, product 
        """
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.product = Product.objects.create(
            user = self.user,
            title = 'Test product',
            description = 'Test product description',
            country = 'Country',
            city = 'City',
            category = 'fruit',
            price = 10.50,
            currency = 'eur',
            available = True,
            quantity = 10,
            units = 'kg'
        )

    def test_slug_is_created(self):
        """
        Test slug is automatically created
        """
        self.assertEqual(self.product.slug, 'test-product')
