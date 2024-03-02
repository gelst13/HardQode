from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Product, Lesson
from .forms import BuyForm
from .utils import EduSys


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


def product_detail(request, pk):
    context = {
        'product': Product.objects.get(id=pk),
        'lessons': Lesson.objects.filter(course=Product.objects.get(id=pk)).all()
    }
    return render(request, 'edu/product_detail.html', context)


def buy_course(request, pk):
    # if request.user.is_authenticated:
    form = BuyForm()
    context = {'form': form,
               'product': Product.objects.get(id=pk)}
    if request.method == 'POST':
        EduSys.enroll_on_course(product_id=pk, user_id=request.user.id)
        return redirect('profile')
    return render(request, 'edu/buy_course.html', context)
