from django.urls import path
from .views import (
    ProductsList,
    AddProduct,
    ProductDetail,
    ProductListFavorite,
    EditProduct,
    ToggleProduct,
    DeleteProduct
)

urlpatterns = [
    path('', ProductsList.as_view(), name='products'),
    path('add/', AddProduct.as_view(), name='add_product'),
    path(
        '<slug:slug>/<int:pk1>/',
        ProductDetail.as_view(),
        name='product_detail'
        ),
    path(
        'favorite/<slug:slug>/<int:product_id>/',
        ProductListFavorite.as_view(),
        name='add_to_favorite'
        ),
    path(
        'edit/<slug:slug>/<int:pk1>/',
        EditProduct.as_view(),
        name='edit_product'
        ),
    path(
        'toggle/<slug:slug>/<int:pk1>/',
        ToggleProduct.as_view(),
        name='toggle_product'
        ),
    path(
        'delete/<slug:slug>/<int:pk1>/',
        DeleteProduct.as_view(),
        name='delete_product'
        ),
]
