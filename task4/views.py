from django.shortcuts import render

def home_view(request):
    return render(request, 'third_task/home.html')

def shop_view(request):
    # Пример списка товаров
    products = {
        'product1': 'Книга "Введение в программирование"',
        'product2': 'Компьютерная мышь',
        'product3': 'Клавиатура',
    }
    return render(request, 'third_task/shop.html', {'products': products})

def cart_view(request):
    return render(request, 'third_task/cart.html')


# task4/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'fourth_task/home.html')

def shop_view(request):
    # Обновлённый список игр
    games = ['Atomic Heart', 'Cyberpunk 2077']
    return render(request, 'fourth_task/shop.html', {'games': games})

def cart_view(request):
    return render(request, 'fourth_task/cart.html')

