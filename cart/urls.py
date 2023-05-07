from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

    # Маршрут "Детали корзины"
    path('', views.cart_detail, name='cart_detail'),
    # Маршрут "Добавление в корзину"
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # Маршрут "Удаление из корзины"
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

]