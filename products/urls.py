from django.urls import path
from .views import ProductsList, AddProduct

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('add/', AddProduct.as_view(), name='add_product'),
]
