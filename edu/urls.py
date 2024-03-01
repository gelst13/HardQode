from django.urls import path
from . import views
from .views import ProductListView


urlpatterns = [
    # path('', views.home, name='edu-home'),
    path('', ProductListView.as_view(), name='edu-home'),
    path('about/', views.about, name='edu-about'),
    path('course/<int:pk>', views.product_detail, name='product-detail'),
    path('course/<int:pk>/buy', views.buy_course, name='buy-course'),
]
