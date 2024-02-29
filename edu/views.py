from django.shortcuts import render


products = [
    {
        'author': 'CoreyMS',
        'name': 'Django crash course',
        'start_date': '01-03-2024',
        'start_time': '10:00',
        'price': '3000'
    },
    {
        'author': 'CoreyMS',
        'name': 'Flask crash course',
        'start_date': '01-03-2024',
        'start_time': '10:00',
        'price': '3000'
    },
]


def home(request):
    context = {
        'title': 'Курсы',
        'products': products
    }
    return render(request, 'edu/home.html', context)


def about(request):
    return render(request, 'edu/about.html', {'title': 'О нас'})
