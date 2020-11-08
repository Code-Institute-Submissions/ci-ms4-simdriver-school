from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataselector, name='dataselector'),
    path('<product_id>/', views.setup_details, name='setup_detail'),
]