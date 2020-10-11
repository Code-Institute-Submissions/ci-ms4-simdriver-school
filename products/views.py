from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ 
    A view to return all products, incuding sorting and search queries
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def packages(request):
    """
    A view to show the available packages
    """

    return render(request, 'products/packages.html')