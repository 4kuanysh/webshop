from django.shortcuts import render

from .models import *

def index(request):
    categories = ProductCategory.objects.all()

    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products
    }

    return render(request, 'products/сatalog.html', context=context)