from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .cart import Cart
from .forms import *


# # Добавление товаров в корзину:
# def cart_add(request, product_id):
#     if request.method == 'POST':
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=product_id)
#         form = CartAddProductForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             cart.add(product=product, quantity=data['quantity'], update_quantity=data['update'])
#         return redirect('cart:cart_detail')


# Добавление товаров в корзину:
def cart_add(request, product_id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cart.add(product=product, quantity=data['quantity'], update_quantity=data['update'])
        return redirect('cart:cart_detail')


# Удаление товаров из корзины:
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# Метод для отображения товаров, добавленных в корзину, исходя из данных в сессии
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    context = {'cart': cart}
    return render(request, 'cart/detail.html', context=context)
