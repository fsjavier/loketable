from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import Product, Favorite


class TestViews(TestCase):
    """
    Test profile views
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

    def test_get_profile_page(self):
        """
        Test profile page response
        """
        response = self.client.get(f'/user/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_favorites_page_logged_in_user(self):
        """
        Test favorites page response for a logged in user
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(f'/user/favorites/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_favorites_page_logged_out_user(self):
        """
        Test logged out user is redirected when trying
        to access favorites url
        """
        response = self.client.get('/user/favorites/')
        self.assertEqual(response.status_code, 302)

    def test_user_can_edit_profile(self):
        """
        Test logged in user can edit own profile
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(f'/user/edit/{self.user.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')

    def test_user_can_not_edit_other_profile(self):
        """
        Test a user can't edit somebody else's profile
        """
        user_2 = User.objects.create_user(
            username='test_user2',
            password='test_password2'
        )
        self.client.login(username='test_user2', password='test_password2')
        response = self.client.get(f'/user/edit/{self.user.id}/')
        self.assertEqual(response.status_code, 403)
