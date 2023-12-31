from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Choice Fields
CATEGORIES = (
    ("meat", "Meat"),
    ("fruit", "Fruit"),
    ("vegetables", "Vegetables"),
    ("wine", "Wine"),
    ("beer", "Beer"),
    ("honey", "Honey"),
    ("nuts", "Nuts"),
    ("cheese", "Cheese"),
    ("mix", "Mix of products"),
    ("other", "Other")
)

CURRENCIES = (
    ('eur', 'EUR'),
    ('gbp', 'GBP'),
    ('usd', 'USD'),
    ('sek', 'SEK')
)

UNIT_CHOICES = (
    ('kg', 'Kg.'),
    ('gr', 'gr.'),
    ('liters', 'l.'),
    ('ml', 'ml.'),
    ('bottle', 'bottle'),
    ('bottles', 'bottles'),
    ('unit', 'unit'),
    ('units', 'units'),
)


class Product(models.Model):
    """
    Model to create a product
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="producer"
        )
    title = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        default="other"
        )
    price = models.FloatField()
    currency = models.CharField(
        max_length=10,
        choices=CURRENCIES,
        default="eur"
        )
    available = models.BooleanField()
    quantity = models.IntegerField(null=False, blank=False)
    units = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default='unit'
    )
    slug = models.SlugField(max_length=200)
    favorited_by = models.ManyToManyField(
        User, related_name='favorites',
        blank=True
    )

    class Meta:
        """
        Order by most recently updated
        """
        ordering = ['-updated_date']

    def __str__(self):
        return self.title

    def currency_display(self):
        """
        Return the currency symbol
        """
        if self.currency == 'eur':
            return '€'
        elif self.currency == 'gbp':
            return '£'
        elif self.currency == 'usd':
            return '$'
        elif self.currency == 'sek':
            return 'SEK'
        else:
            return ''

    def category_icon_url(self):
        """
        Return the category icon.
        """
        if self.category == 'meat':
            return 'icons/meat.webp'
        elif self.category == 'fruit':
            return 'icons/fruits.webp'
        elif self.category == 'vegetables':
            return 'icons/vegetables.webp'
        elif self.category == 'wine':
            return 'icons/wine.webp'
        elif self.category == 'beer':
            return 'icons/beer.webp'
        elif self.category == 'honey':
            return 'icons/honey.webp'
        elif self.category == 'nuts':
            return 'icons/nuts.webp'
        elif self.category == 'cheese':
            return 'icons/cheese.webp'
        elif self.category == 'mix':
            return 'icons/food_mix.webp'
        else:
            return 'icons/food_mix.webp'

    def save(self, *args, **kwargs):
        """
        Creates a slug when the user adds a product.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
