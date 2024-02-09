from django.shortcuts import render


def login(request):
    context = {
        'title': 'Food - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Food - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Food - Кабинет'
    }
    return render(request,'users/profile.html', context)


def logout(request):
    pass
