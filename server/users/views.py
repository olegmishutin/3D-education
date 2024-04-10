from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            User.objects.create_user(**registerForm.cleaned_data)

            return render(request, 'index.html', {'regMessage': 'Успешная регистрация!'})
        return render(request, 'index.html', {'regMessage': 'Ошибка в регистрации!'})
    return HttpResponse(status=404)


def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
            return render(request, 'index.html', {'logMessage': 'Пользователь не найден!'})
        return render(request, 'index.html', {'logMessage': 'Ошибка входа!'})
    return HttpResponse(status=404)


def logoutUser(request):
    if request.method == 'GET' and request.user.is_authenticated:
        logout(request)
        return redirect('index')
    return request.META.get('HTTP_REFERER')
