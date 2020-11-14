from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataselector, name='dataselector'),
    path('add/', views.add_datapack, name='add_datapack'),
    path('edit/<datapack_id>/', views.edit_datapack, name='edit_datapack'),
    path('delete/<datapack_id>/', views.delete_datapack,
         name='delete_datapack'),
    path('<product_id>/', views.setup_details, name='setup_detail'),
]
