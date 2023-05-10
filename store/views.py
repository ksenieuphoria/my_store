from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *  # Импортируем все существующие модели
from .forms import *  # Импортируем все существующие модели
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from cart.forms import *


# Метод маршрута "Главная страница"
# http://127.0.0.1:8000
def main(request):
    return render(request, "store/main.html")


# Метод маршрута "Список всех продуктов и их фильтрация по категориям"
# http://127.0.0.1:8000/store
def store(request):
    if request.method == 'GET':
        products = DataBase.read(Product, mode="all")
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = CategoryForm()
        context = {"products": products, "form": form, "page_obj": page_obj}
        return render(request, 'store/product/store.html', context=context)
    if request.method == 'POST':
        # Получение данных из формы
        category = request.POST.get("category")
        if category == "Показать всё":
            products = DataBase.read(Product, mode="all")
            paginator = Paginator(products, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            form = CategoryForm()
            context = {"products": products, "form": form, "page_obj": page_obj}
            return render(request, 'store/product/store.html', context=context)
        else:
            products = Product.objects.filter(category__name=category)
            paginator = Paginator(products, 8)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            print("$$$", products)
            form = CategoryForm()
            context = {"products": products, "form": form, "page_obj": page_obj}
            return render(request, 'store/product/store.html', context=context)


# # Метод маршрута "Список всех продуктов и их фильтрация по категориям"
# # http://127.0.0.1:8000/store
# def store(request):
#     if request.method == 'GET':
#         products = DataBase.read(Product, mode="all")
#         form = CategoryForm()
#         form_cart = CartAdd_Form()
#         context = {"products": products, "form": form, "form_cart": form_cart}
#         return render(request, 'store/product/store.html', context=context)
#     if request.method == 'POST':
#         # Получение данных из формы
#         category = request.POST.get("category")
#         if category == "Показать всё":
#             products = DataBase.read(Product, mode="all")
#             form = CategoryForm()
#             context = {"products": products, "form": form}
#             return render(request, 'store/product/store.html', context=context)
#         else:
#             products = Product.objects.filter(category__name=category)
#             print("$$$", products)
#             form = CategoryForm()
#             context = {"products": products, "form": form}
#             return render(request, 'store/product/store.html', context=context)


# Метод маршрута "Продукт" /product/<int:product_id>
# http://127.0.0.1:8000/product/3
def product_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=product_id)  # get_object_or_404 - Возвращает определённый объект
        # из модели в зависимости от значения его первичного ключа, или выбрасывает исключение Http404,
        # если данной записи не существует
        # Создаём форму для указания количества продукта
        cart_product_form = CartAddProductForm()
        # Передаём в context продукт и форму
        context = {"product": product, "cart_product_form": cart_product_form}
        return render(request, "store/product/product.html", context=context)


# Метод маршрута "О компании" /about
def about(request):
    return render(request, "store/about.html")

def test(request):
    return render(request, "test.html")


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
            for elm in qs.values():
                result.append(elm)
            return result
        if mode == "name":  # Финальный список из (названий)
            result = []
            for elm in qs:
                result.append(elm.name)
            return result
