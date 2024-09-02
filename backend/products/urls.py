from django.urls import path
from . import views

urlpatterns = [
    # Other URLs...
    path('add_product/', views.add_product, name='add_product'),
    path('',views.get_products,name='get_products'),
]
