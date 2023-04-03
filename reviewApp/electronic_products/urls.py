from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('', views.home, name='electronic_products-home'),
    path('about/', views.about, name='electronic_products-about'),
    path('contact/', views.contact, name='electronic_products-contact'),
    path('product/', views.product, name='electronic_products-product'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] 