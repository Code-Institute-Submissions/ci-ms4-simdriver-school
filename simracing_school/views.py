from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView


class Facebook(RedirectView):
    url = 'https://facebook.com'
