from django.urls import path
from . import views

app_name = 'store'  # с помощью переменной app_name определено пространство имен приложения.
# это позволяет организовать URL по приложениям и использовать имена, ссылаясь на них.

urlpatterns = [

    # Маршрут "Главная страница"
    path('', views.main, name='main'),
    # Маршрут "Детали продукта"
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    # Маршрут "Список всех продуктов"
    path('store', views.store, name='store'),
    # Маршрут "О компании"
    path('about', views.about, name='about'),
    path('test', views.test, name='test'),

]
