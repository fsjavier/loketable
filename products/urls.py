from django.urls import path
from .views import ProductsList, AddProduct, ProductDetail

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('add/', AddProduct.as_view(), name='add_product'),
    path('<slug:slug>/<int:pk1>', ProductDetail.as_view(), name='product_detail'),
]
