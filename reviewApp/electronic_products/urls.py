from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='electronic_products-home'),
    path('about/', views.about, name='electronic_products-about'),
    path('contact/', views.contact, name='electronic_products-contact'),
    path('product/', views.product, name='electronic_products-product'),
]