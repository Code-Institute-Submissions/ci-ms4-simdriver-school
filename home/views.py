from django.shortcuts import render, redirect
from products.models import Product, Category

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faqs(request):
    """ A view to return the faqs page """

    return render(request, 'faqs.html')


def packages(request):
    """
    A view to show the available packages
    """

    return render(request, 'packages.html')

"""
def datapacks(request):
    return render(request, 'home/datapacks.html')


def dataselector(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    imsa = Product.objects.filter(category__name='imsa_series')

    context = {
        'products': products,
        'categories': categories,
        'imsa': imsa,
    }
    return render(request, 'home/dataselector.html', context)
"""