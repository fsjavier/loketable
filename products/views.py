from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductsList(generic.ListView):
    """ View all products """
    model = Product
    queryset = Product.objects.filter(available=True).order_by('-updated_date')
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6
