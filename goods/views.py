from django.shortcuts import render
from goods.models import Categories, Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Food delivery - Меню',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/product.html')
