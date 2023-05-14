from django.urls import path
from . import views

app_name = 'cart'  # с помощью переменной app_name определено пространство имен приложения.
# это позволяет организовать URL по приложениям и использовать имена, ссылаясь на них.

urlpatterns = [

    # Маршрут "Детали корзины"
    path('', views.cart_detail, name='cart_detail'),
    # Маршрут "Добавление в корзину"
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # Маршрут "Удаление из корзины"
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

]