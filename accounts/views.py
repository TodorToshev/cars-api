from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.utils.decorators import method_decorator
from functools import wraps


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect("cars:all")
        messages.error(request, 'Registration failed.')
    else:
        form = UserRegistrationForm()
    return render(request, template_name='registration/registration.html', context={'form': form})
