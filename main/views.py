from django.shortcuts import render

from .models import Product


def home(request):
    ps = Product.objects.all()
    return render(request, 'index.html', {'ps': ps})
