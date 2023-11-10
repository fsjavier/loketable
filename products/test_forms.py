from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Test product form
    """

    def test_title_is_required(self):
        """
        Test title is required
        """
        form = ProductForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
    
    def test_description_is_required(self):
        """
        Test description is required
        """
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_country_is_required(self):
        """
        Test country is required
        """
        form = ProductForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_city_is_required(self):
        """
        Test city is required
        """
        form = ProductForm({'city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors.keys())
        self.assertEqual(form.errors['city'][0], 'This field is required.')

    def test_category_is_required(self):
        """
        Test category is required
        """
        form = ProductForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_quantity_is_required(self):
        """
        Test quantity is required
        """
        form = ProductForm({'quantity': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'This field is required.')

    def test_units_is_required(self):
        """
        Test units is required
        """
        form = ProductForm({'units': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('units', form.errors.keys())
        self.assertEqual(form.errors['units'][0], 'This field is required.')

    def test_price_is_required(self):
        """
        Test price is required
        """
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_currency_is_required(self):
        """
        Test currency is required
        """
        form = ProductForm({'currency': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('currency', form.errors.keys())
        self.assertEqual(form.errors['currency'][0], 'This field is required.')
