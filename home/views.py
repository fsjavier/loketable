from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Index(TemplateView):
    """
    Home Page view
    """
    template_name = 'home/index.html'

    def get(self, request):
        """
        Check if user is authenticated. If it is, redirect
        to Products, if not render the template.
        """
        if request.user.is_authenticated:
            return redirect('products')
        else:
            return render(request, self.template_name)
