from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faqs(request):
    """ A view to return the faqs page """

    return render(request, 'faqs.html')
