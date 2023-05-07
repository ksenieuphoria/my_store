from django.db import models
from django.urls import reverse

'''  --- ШПАРГАЛКА Варианты параметров доступных в полях моделей: ---
null - Разрешить хранить это поле пустым в БД (True)
blank - Разрешить формам Django игнорировать это поле (True) + Разрешить хранить это поле пустым в БД
default - Значение по умолчанию для поля
primary_key - Первичный ключ для поля (уникальное)
choices - Предоставление выбора из вариантов значение (не используем)
on_delete - Разные сценарии при удалении главной сущности (обязательно для ForeignKey) (CASCADE, PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING)

help_text - ... При заполнении(добавлении) модели из админки (Подсказка снизу под полем)
verbose_name - ... При заполнении(добавлении) модели из админки (Текстовая метка поля)

slug - Для построения удобночитаемых URL’ов
db_index - Для ускорения запросов по базе данных (Если True, для этого поля будет создан индекс базы данных)
unique - Если True, это поле должно быть уникальным во всей таблице.
'''


# Модель Категория одежды (Category)
# Поля: name(Название), slug(для построения URL)
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, help_text="Введите наименование категории", verbose_name="Категория")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    objects = models.Model

    # При просмотре всей модели из админки (поле, которое будет отображаться в таблице)
    def __str__(self):
        return self.name

    # [ВНУТРЕННИЙ МЕТОД] Возвращающий ссылку на категорию
    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])

    # Настройки перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


# Модель Одежда (Product)
# Поля: Поля (связи): category(Category-ForeignKey)
# Поля: name(Название), price(Цена), image(Картинка), description(Описание), available(Доступность)
class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='products', help_text="Выберете категорию", verbose_name="Категория")
    name = models.CharField(max_length=60, help_text="Введите наименование предмета", verbose_name="Наименование")
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="URL")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Введите цену предмета", verbose_name="Цена")
    image = models.ImageField(null=True, blank=True, help_text="Загрузите изображение предмета", verbose_name="Изображение")
    description = models.TextField(blank=True, null=True, help_text="Введите описание продукта", verbose_name="Описание продукта")
    available = models.BooleanField(default=True, help_text="Введите статус наличия", verbose_name="В наличии")
    objects = models.Model

    # При просмотре всей модели из админки (поле, которое будет отображаться в таблице)
    def __str__(self):
        return self.name

    # Настройки перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Продукт"  # Название модели в единственном числе
        verbose_name_plural = "Продукты"  # Название модели во множественном числе
        ordering = ["name"]  # Поле по которому будет происходить сортировка

