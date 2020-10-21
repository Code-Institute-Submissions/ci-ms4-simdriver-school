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
    gold_package = Product.objects.filter(category__name='gold_package')
    context = {
        'gold_package': gold_package,
    }
    return render(request, 'home/packages.html', context)

"""
def datapacks(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'home/datapacks.html', context)


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