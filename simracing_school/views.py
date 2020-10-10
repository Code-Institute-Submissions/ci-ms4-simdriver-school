from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

""" Social Media links """
class Facebook(RedirectView):
    url = 'https://facebook.com'


class Instagram(RedirectView):
    url = 'https://instagram.com'


class Twitter(RedirectView):
    url = 'https://twitter.com'


""" External Site Links """
class iRacing(RedirectView):
    url = 'https://iracing.com'


class TradePaints(RedirectView):
    url = 'https://tradingpaints.com'


class CrewChief(RedirectView):
    url = 'http://thecrewchief.org'
