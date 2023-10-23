from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
        )
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    contact = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """ Create user profile """
    if created:
        Profile.objects.create(user=instance)


class Favorite(models.Model):
    """ Records of users who saved favorites """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorited"
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="favorite_product"
        )

    def __str__(self):
        return self.user.username
