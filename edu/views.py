from django.shortcuts import render
from .models import Product


def home(request):
    context = {
        'title': 'Курсы',
        'products': Product.objects.all()
    }
    return render(request, 'edu/home.html', context)


def about(request):
    return render(request, 'edu/about.html', {'title': 'О нас'})
