from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product, Lesson


# def home(request):
#     context = {
#         'title': 'Курсы',
#         'products': Product.objects.all()
#     }
#     return render(request, 'edu/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'edu/home.html'
    context_object_name = 'products'
    ordering = ['author', 'title']
    

def about(request):
    return render(request, 'edu/about.html', {'title': 'О нас'})


def product_detail(request, id):
    context = {
        'product': Product.objects.all()[id],
        'lessons': Lesson.objects.filter(course=Product.objects.all()[id]).all()
    }
    return render(request, 'edu/home.html', context)


class ProductDetailView(DetailView):
    model = [Product, Lesson]
    context_object_name = 'product'


