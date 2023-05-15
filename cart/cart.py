from decimal import Decimal
from django.conf import settings
from store.models import Product

'''
Класс Cart (Корзина), который отвечает за работу с корзинами покупок.
При инициализации объекта этого класса в метод __init__ передается
объект запроса request. Мы записываем текущую сессию в атрибут класса self.session
(она равна сессии из запроса request.session), чтобы иметь к ней доступ в
других методах класса. Затем пытаемся получить данные корзины, обращаясь к 
self.session.get(settings.CART_SESSION_ID). Если не получаем объект корзины,
то создаем ее как пустой словарь в сессии. В этом словаре ключами будут
являться id товаров, а значениями - количество и цена. Так мы будем уверены,
что товар не добавлен в корзину больше одного раза. Хранение корзины в 
виде словаря упростит доступ к ее элементам.

Благодаря промежуточному слою MIDDLEWARE текущая сессия становится доступна в объекте запроса, request, 
и мы можем обратиться к ней через запись request.session. (это словарь)
Информация сессии сохраняется в базе данных на стороне сервера.
'''


# Класс Корзины (Cart), который отвечает за работу с корзинами покупок
class Cart(object):
    session = None  # Текущая сессия
    cart = None  # Корзина

    # Метод __init__. Инициализация объекта корзины
    def __init__(self, request):
        self.session = request.session  # Делаем запрос к текущей сессии, записываем его в атрибуте класса self.session(это словарь)
        cart = self.session.get(settings.CART_SESSION_ID)  # Получаем через метод словаря dict.get() значение словаря по ключу и записываем в cart
        if not cart:  # Если значение ключа (то есть словарь) пустой, то:
            cart = self.session[settings.CART_SESSION_ID] = {}  # Сохраняем в сессии пустой словарь {"cart": {} }
        self.cart = cart  # Присваиваем переменной класса содержимое словаря cart. self.cart это СЛОВАРЬ!!!

    # 1. Метод add - Добавление id товара в {} словарь cart
    def add(self, product, quantity=1, update_quantity=False):
        # Используем id товара как ключ в словаре cart
        product_id = str(product.id)  # Ключ словаря должен быть строкой! делаем product.id строкой
        # Если id такого продукта нет в корзине, то:
        if product_id not in self.cart:
            # Создаём новый ключ и значение в словаре cart
            # пример: self.cart['5'] = {'quantity': 0, 'price': '119'}
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
            # И далее можем получить созданное значение ключа.
        # Если update_quantity=True, то:
        if update_quantity:
            #  Присваиваем ключу количество ключа product.id актуальное переданное количество
            self.cart[product_id]['quantity'] = quantity
        # Иначе, если update_quantity=False, то:
        else:
            # Увеличиваем значение quantity на 1
            self.cart[product_id]['quantity'] += quantity
        # Вызываем внутренний метод def save(self): класса Cart - помечаем сессию как измененную
        print("blabla", self.cart)
        self.save()

    # 2. Метод save - Обновление количества товаров в корзине
    def save(self):
        # Помечаем сессию как измененную
        self.session.modified = True

    # 3. Метод remove - Удаление товаров из корзины
    def remove(self, product):
        # Удаление товара из корзины
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # 4. Метод __iter__ для прохождения в цикле по объектам Product
    def __iter__(self):
        # Шаг 1. Записываем в переменную "product_ids" ключи СЛОВАРЯ(dict) "self.cart"
        # self.cart это СЛОВАРЬ(dict)!
        # {'4': {'quantity': 1, 'price': Decimal('119.00'), 'product': <Product: Джинсовое мини-платье>, 'total_price': Decimal('119.00')}, ... }
        # Для этого используем метод dict.keys()
        # Метод dict.keys() возвращает ключи в словаре
        print("Корзина: ", self.cart)
        product_ids = self.cart.keys()  # метод dict.keys() возвращает ключи в словаре
        # Ключи словаря self.cart: (['4', '5', '9', '6'])
        print("Ключи словаря self.cart: ", product_ids)  # product_ids dict_keys(['4', '5', '9', '6'])
        # Получаем объекты модели Product и передаем их в корзину
        products = Product.objects.filter(id__in=product_ids)  # Оператор __in означает, что id равно одному из значений списка product_ids(входит В список)
        # Products - это QuerySet! <QuerySet [<Product: Джинсовое мини-платье>, <Product: Укороченная джинсовая куртка>,
        print("QuerySet products: ", products)
        # Делаем копию словаря и записываем его в переменную cart
        cart = self.cart.copy()
        print("cartttt", cart)
        # По QuerySet мы можем пробежаться циклом for
        # для того, чтобы создать новую пару ключ[имя продукта]: значение[имя продукта]
        for product in products:
            print(product)
            cart[str(product.id)]['product'] = product
        # Метод dict.values() возвращает значения в словаре
        print("Значения в словаре cart: ", cart.values())
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # 5. Метод len - возвращает общее количество единиц товаров в корзине
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # 6. Метод get_total_price - для подсчета общей стоимости корзины
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # 7. Метод clear - очистка корзины
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
