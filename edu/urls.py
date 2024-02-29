from django.urls import path
from . import views
from .views import ProductDetailView


urlpatterns = [
    path('', views.home, name='edu-home'),
    path('about/', views.about, name='edu-about'),
    path('course/<int:pk>', views.product_detail, name='product-detail'),
]
