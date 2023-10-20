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

    def currency_display(self):
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
        if self.category == 'meat':
            return '/icons/meat.png'
        elif self.category == 'fruit':
            return '/icons/fruits.png'
        elif self.category == 'vegetables':
            return '/icons/vegetables.png'
        elif self.category == 'wine':
            return '/icons/wine.png'
        elif self.category == 'beer':
            return '/icons/beer.png'
        elif self.category == 'honey':
            return '/icons/honey.png'
        elif self.category == 'nuts':
            return '/icons/nuts.png'
        elif self.category == 'cheese':
            return '/icons/cheese.png'
        elif self.category == 'mix':
            return '/icons/food_mix.png'
        else:
            return '/icons/food_mix.png'
            # ("other", "Other")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
