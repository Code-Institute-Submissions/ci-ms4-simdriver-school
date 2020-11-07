from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataselector, name='dataselector'),
    path('setups/', views.datapacks, name='setups'),
]