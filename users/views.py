from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Профиль создан для {username}!')
            return redirect('edu-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
