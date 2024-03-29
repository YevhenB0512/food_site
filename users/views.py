from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from carts.models import Cart
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f'{username} Вы вошли в аккаунт')

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return redirect(request.POST.get('next'))
                
                return redirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Food - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, f'{user.username} Вы вошли зарегистрировались и вошли в аккаунт')
            return redirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Food - Регистрация',
        'form': form,
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return redirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Food - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username} Вы вышли из аккаунта')
    auth.logout(request)
    return redirect(reverse('main:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')