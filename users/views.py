from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Профиль создан для {username}!')
            return redirect('edu-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
