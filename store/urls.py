from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [

    # Маршрут "Главная страница"
    path('', views.main, name='main'),
    # Маршрут "Список всех продуктов"
    path('store', views.store, name='store'),
    # Маршрут "Детали продукта"
    path('product/<int:product_id>', views.product_detail, name='product_detail'),

]
