from sqlite3 import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderModelForm
from cart.cart import Cart
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save()
            print("cart before order: ", cart)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            request.session['order_id'] = order.id
            context = {"order": order}
            # return redirect(reverse('payment:process'))
            return render(request, 'orders/created.html', context=context)
        else:
            form = OrderModelForm()
            text = "проверьте правильность заполнения формы"
            context = {"cart": cart, "form": form, "text": text}
            return render(request, 'orders/create.html', context=context)
    if request.method == 'GET':
        form = OrderModelForm()
        context = {"cart": cart, "form": form}
        return render(request, 'orders/create.html', context=context)


# Класс содержащий ВНУТРЕННЮЮ работу с БД
class DataBase:

    @staticmethod
    # Чтение из таблицы "model" элементов удовлетворяющих тому что передаем в {} через "kwargs"
    def read(model, mode="all", **kwargs):
        # .count() - метод возвращающий количество
        if mode == "all":  # Получить данные для [всех объектов]
            result = model.objects.all()
            return list(result.values())
        if mode == "filter":  # Получить данные [все которые = фильтр]
            result = model.objects.filter(**kwargs)
            return list(result.values())
        if mode == "exclude":  # Получить данные [все которые = не фильтр]
            result = model.objects.exclude(**kwargs)
            return list(result.values())
        if mode == "get":  # Получить данные для [одного объекта]
            result = model.objects.get(**kwargs)  # id/pk одно и тоже
            print(result, type(result))
            return [result]

    @staticmethod
    # Запись в таблицу "model" элемента с полями которые передаем в {} через "kwargs"
    def write(model, **kwargs):
        model(**kwargs).save()  # или Person.objects.create(**kwargs)

    @staticmethod
    # Обновление объекта с "elm_id" в таблице "model", а именно перезапись полей на те, которые в {} через "kwargs"
    def update(model, elm_id, **kwargs):
        model.objects.filter(id=elm_id).update(**kwargs)

    @staticmethod
    # Удаление из таблицы "model" записи, удовлетворяющей фильтру переданному в {} через "kwargs"
    def delete(model, **kwargs):
        model.objects.filter(**kwargs).delete()

    @staticmethod
    # Создание нового пользователя с "login" "password" "email" (все параметры обязательны)
    def create_user(login, password, email):
        try:
            User.objects.create_user(login, email, password).save()
        except IntegrityError:
            pass

    @staticmethod
    # Преобразование queryset в list в зависимости от режима "mode"
    def queryset_to_list(qs, mode=""):
        if mode == "elements":  # Финальный список из (элементов)
            result = []
            for elm in qs:
                result.append(elm)
            return result
        if mode == "name":  # Финальный список из (названий)
            result = []
            for elm in qs:
                result.append(elm.name)
            return result
