from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product
from profiles.models import Favorite


class TestViews(TestCase):
    """
    Test products views
    """

    def setUp(self):
        """
        Create a test user and product
        """
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        self.product = Product.objects.create(
            user=self.user,
            title='Test product',
            description='Test product description',
            country='Country',
            city='City',
            category='fruit',
            price=10.50,
            currency='eur',
            available=True,
            quantity=10,
            units='kg'
        )

    def test_get_products_page(self):
        """
        Test products page response
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_details_page(self):
        """
        Test product details page response
        """
        response = self.client.get(
            f'/products/{self.product.id}/{self.product.slug}/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product_page_not_logged_in(self):
        """
        Test logged out user is redirected when trying
        to access add product url
        """
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)

    def test_get_add_product_page_logged_in(self):
        """
        Test logged in user can access add product page
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_can_add_product(self):
        """
        Test user can add a product
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post('/products/add/', {
            'title': self.product.title,
            'description': self.product.description,
            'country': self.product.country,
            'city': self.product.city,
            'category': self.product.category,
            'price': self.product.price,
            'currency': self.product.currency,
            'available': self.product.available,
            'quantity': self.product.quantity,
            'units': self.product.units
        })
        self.assertRedirects(response, f'/user/{self.user.id}/')

    def test_user_can_add_and_remove_product_from_favorites(self):
        """
        Test user can add and remove a product from favorites
        """
        self.client.login(username='test_user', password='test_password')
        # Add product to favorites
        response = self.client.post(
            f'/products/favorite/{self.product.id}/{self.product.slug}/'
        )
        self.assertRedirects(response, '/products/')
        # Check that the product is in favorites
        favorite_items = Favorite.objects.filter(
            user=self.user, product=self.product
        )
        self.assertEqual(len(favorite_items), 1)
        # Remove product from favorites
        response = self.client.post(
            f'/products/favorite/{self.product.id}/{self.product.slug}/'
        )
        self.assertRedirects(response, '/products/')
        # Check that the product is no longer in favorites
        favorite_items = Favorite.objects.filter(
            user=self.user, product=self.product
        )
        self.assertEqual(len(favorite_items), 0)
