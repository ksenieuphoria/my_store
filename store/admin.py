from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


#  Регистрация и настройка модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


#  Регистрация и настройка модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'show_image', 'category', 'price', 'available']
    list_filter = ['available', 'category']
    prepopulated_fields = {"slug": ("name",)}

    def show_image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'>".format(obj.image.url))
        return "None"

    show_image.__name__ = "Изображение"

