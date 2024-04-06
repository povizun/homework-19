from django.shortcuts import render

from catalog.models import Product


def index(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Пользователь {name} ({phone}) оставил сообщение: {message}')

    return render(request, 'catalog/contacts.html')
