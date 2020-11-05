from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataselector, name='dataselector'),
    path('datapacks/', views.datapacks, name='datapacks'),
]