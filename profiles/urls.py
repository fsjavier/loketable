from django.urls import path
from .views import Profiles, EditProfile
from products.views import FavoriteProductsList

urlpatterns = [
    path('<int:pk>/', Profiles.as_view(), name='profile'),
    path('edit/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path(
        'favorites/',
        FavoriteProductsList.as_view(),
        name='favorite_products'
        ),
]
