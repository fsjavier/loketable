from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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


class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="producer"
        )
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
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
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['-updated_date']

    def __str__(self):
        return self.title
