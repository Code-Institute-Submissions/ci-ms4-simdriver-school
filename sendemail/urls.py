from django.contrib import admin
from django.urls import path

from .views import successView, contactView

urlpatterns = [
    path('contactus/', contactView, name='contact'),
    path('success/', successView, name="success"),
]