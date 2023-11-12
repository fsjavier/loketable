from django.urls import path
from .views import (
    ProductsList,
    AddProduct,
    ProductDetail,
    ProductListAddFavorite,
    EditProduct,
    ToggleProduct,
    DeleteProduct
)

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('add/', AddProduct.as_view(), name='add_product'),
    path(
        '<int:pk>/<slug:slug>/',
        ProductDetail.as_view(),
        name='product_detail'
    ),
    path(
        'favorite/<int:product_id>/<slug:slug>/',
        ProductListAddFavorite.as_view(),
        name='add_to_favorite'
    ),
    path(
        'edit/<int:pk>/<slug:slug>/',
        EditProduct.as_view(),
        name='edit_product'
    ),
    path(
        'toggle/<int:pk>/<slug:slug>/',
        ToggleProduct.as_view(),
        name='toggle_product'
    ),
    path(
        'delete/<int:pk>/<slug:slug>/',
        DeleteProduct.as_view(),
        name='delete_product'
    ),
]
