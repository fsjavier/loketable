from django.urls import path
from .views import ProductsList

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
]
