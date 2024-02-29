from django.shortcuts import render


products = [
    {
        'author': 'CoreyMS',
        'title': 'Django crash course',
        'start_date_time': '01-03-2024 10:00 MSK',
        'price': '3000.00'
    },
    {
        'author': 'CoreyMS',
        'title': 'Flask crash course',
        'start_date_time': '01-03-2024 10:00 MSK',
        'price': '3000.00'
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
