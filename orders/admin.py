from django.contrib import admin
from .models import OrderInformation, OrderItem


#  Регистрация и настройка модели OrderInformation
@admin.register(OrderInformation)
class OrderInformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']


#  Регистрация и настройка модели OrderItem
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']