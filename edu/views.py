from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Lesson, Team
from .forms import BuyForm
from .utils import EduSys

from users.models import Profile


def home(request):
    context = {
        'title': 'Курсы',
        'courses': Product.objects.all()
    }
    return render(request, 'edu/home.html', context)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'edu/home.html'
#     context_object_name = 'products'
#     ordering = ['author', 'title']
    

def about(request):
    return render(request, 'edu/about.html', {'title': 'О нас'})


def course_detail(request, pk):
    context = {
        'course': Product.objects.get(id=pk),
        'lessons': Lesson.objects.filter(course=Product.objects.get(id=pk)).all()
    }
    return render(request, 'edu/course_detail.html', context)


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Product
    fields = ['author', 'title', 'date_msk', 'price', 'min_users', 'max_users', 'number_of_lessons']
    template_name = 'edu/course_detail.html'
    context_object_name = 'course'

    # def test_func(self):
    #     course = self.get_object()
    #     print(course.title)
    #     # cluster = course.author[:1] + course.title[:1]
    #     # if self.request.user.profile.team.name.startswith(cluster):
    #     if self.request.user.profile.team in Team.objects.filter(course=course).all():
    #         print('test passed')
    #         return True
    #     return False


class VideoListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """Видео-уроки доступны для пользователей, оплативших курс и зачисленных в группу."""
    model = Lesson
    fields = ['title', 'video_link', 'course']
    template_name = 'edu/video_list.html'
    context_object_name = 'objects'
    
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))  # kwargs - query params
        # course = get_object_or_404(Product, id=self.request.user.profile.course.id)
        course = get_object_or_404(Product, id=self.kwargs.get('pk'))
        print(course)
        return Lesson.objects.filter(course=course)  # .all()

    def test_func(self):
        course = get_object_or_404(Product, id=self.kwargs.get('pk'))
        print(course)
        if self.request.user.profile.course == course:
            print('test passed')
            return True
        return False


def buy_course(request, pk):
    # if request.user.is_authenticated:
    form = BuyForm()
    context = {'form': form,
               'product': Product.objects.get(id=pk)}
    if request.method == 'POST':
        EduSys.enroll_on_course(product_id=pk, user_id=request.user.id)
        return redirect('profile')
    return render(request, 'edu/buy_course.html', context)
