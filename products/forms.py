from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """ Form to add a product """
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'country',
            'city',
            'image',
            'category',
            'price',
            'currency',
            'available'
        ]

        labels = {
            'title': 'Product Name',
            'description': 'Description',
            'country': 'Product Country',
            'city': 'Product City',
            'image': 'Product Photo',
            'category': 'Category',
            'price': 'Price',
            'currency': 'Currency',
            'available': 'Is currently available?'
        }
