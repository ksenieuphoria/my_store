from django.contrib import admin
from .models import OrderInformation, OrderItem



@admin.register(OrderInformation)
class OrderInformationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity']