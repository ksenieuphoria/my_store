from django.urls import path
from . import views

app_name = 'orders'  # с помощью переменной app_name определено пространство имен приложения.
# это позволяет организовать URL по приложениям и использовать имена, ссылаясь на них.

urlpatterns = [

    path('create', views.order_create, name='order_create'),
    path('created', views.order_create, name='order_created'),

]