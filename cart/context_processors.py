from .cart import Cart


def cart(request):
    context = {'cart': Cart(request)}
    return context


"""
Это обычная функция, которая принимает объект запроса в качестве аргумента и возвращает словарь, 
добавляемый в контекст запроса.
"""