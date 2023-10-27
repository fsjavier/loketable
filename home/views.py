from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('products')
        else:
            return render(request, self.template_name)
