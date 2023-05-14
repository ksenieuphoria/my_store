from django.contrib import admin
from .models import OrderInformation, OrderItem


#  Регистрация и настройка модели OrderInformation
@admin.register(OrderInformation)
class OrderInformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']

# Объявление ВНУТРЕННЕЙ модели "BookInstance" (дополнительная к основной)
    class OrderItemInline(admin.TabularInline):
        model = OrderItem

    # Дополняем ОСНОВНУЮ "Book" модель дополнительной (ВНУТРЕННЕЙ) "BookInstanceInline"
    inlines = [OrderItemInline]


#  Регистрация и настройка модели OrderItem
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']