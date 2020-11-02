from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('upgrade_cart/', views.upgrade_to_gold, name='upgrade_to_gold'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
