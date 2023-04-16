from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostListView2, PostDetailView2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', views.home, name='electronic_products-home'),
    path('about/', views.about, name='electronic_products-about'),
    path('contact/', views.contact, name='electronic_products-contact'),
    path('product/', views.product, name='electronic_products-product'),
    path('review/<int:pk>', PostDetailView.as_view(), name='review-detail'),
    path('review/new/', PostCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', PostUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', PostDeleteView.as_view(), name='review-delete'),
    path('smartTv/', views.smartTv, name='electronic_products-SmartTv'),
    path('product/', PostListView2.as_view(), name='product-detail'),
    path('product/<int:pk>', PostDetailView2.as_view(), name='product-detail'),
    path('smartTv/', views.smartTv, name='electronic_products-SmartTv'),
    path('smartwatch/', views.smartwatch, name='electronic_products-smartwatch'),
    path('smartphone/', views.smartphone, name='electronic_products-smartphone'),
    path('tablet/', views.tablet, name='electronic_products-tablet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)