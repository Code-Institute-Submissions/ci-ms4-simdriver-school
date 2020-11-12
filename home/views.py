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


""" 404 Error Custom Page """
def error_404_view(request, exception):
    return render(request, '404.html')


""" 500 Error Custom Page """
def error_500_view(request):
    return render(request, '500.html')
