from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='edu-home'),
    path('about/', views.about, name='edu-about'),
    path('about/', views.about, name='edu-about'),
]