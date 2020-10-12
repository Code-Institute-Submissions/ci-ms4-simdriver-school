from django.shortcuts import render, redirect

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
