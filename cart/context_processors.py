from .cart import Cart


def cart(request):
    context = {'cart': Cart(request)}
    return context

"""
Это обычная функция, которой в качестве объекта запроса передаётся request, и которая должна возвращать нам словарь
"""