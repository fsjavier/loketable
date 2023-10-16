from django.shortcuts import render
from django.views import generic
from .models import Product
from .forms import ProductForm


class ProductsList(generic.ListView):
    """ View all products """
    model = Product
    queryset = Product.objects.filter(available=True).order_by('-updated_date')
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 6


class AddProduct(generic.CreateView):
    """ Add a product """
    template_name = 'products/add_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/products'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)


class ProductDetail(generic.DetailView):
    """ View product details """
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'
