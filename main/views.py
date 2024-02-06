from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories


def index(request):
    context = {
        'title': 'Food delivery-Главная',
        'content': 'Food delivery',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Food delivery-О нас',
        'content': 'Food delivery',
    }
    return render(request, 'main/about.html', context)