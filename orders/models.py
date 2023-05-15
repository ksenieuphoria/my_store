from django.db import models
from store.models import Product


# Модель Покупатель (главная таблица) для сохранения информации о покупателе (адресе доставки)
# и флаг paid, который по умолчанию равен False
class OrderInformation(models.Model):
    name = models.CharField(max_length=20, help_text="Введите имя покупателя", verbose_name="Имя покупателя")
    email = models.EmailField(help_text="Введите e-mail", verbose_name="E-mail")
    address = models.CharField(max_length=50, help_text="Введите адрес", verbose_name="Адрес")
    city = models.CharField(max_length=20, help_text="Введите город", verbose_name="Город")
    created = models.DateTimeField(auto_now_add=True, help_text="Дата создания заказа",
                                   verbose_name="Дата создания заказа")
    updated = models.DateTimeField(auto_now=True, help_text="Дата изменения заказа",
                                   verbose_name="Дата изменения заказа")
    paid = models.BooleanField(default=False, help_text="Оплачен", verbose_name="Оплачен")

    class Meta:
        verbose_name = "Покупатель"  # Название модели в единственном числе
        verbose_name_plural = "Покупатели"  # Название модели во множественном числе
        ordering = ('created',)

    def __str__(self):
        return 'Покупатель №{} Имя: {}'.format(self.id, self.name)

    # Метод get_total_cost(), чтобы получить общую стоимость товаров в заказе
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


# Модель Заказ (то, что было в корзине) (второстепенная.таблица)
class OrderItem(models.Model):
    order = models.ForeignKey(OrderInformation, related_name='order', on_delete=models.CASCADE, verbose_name="Информация о заказе")
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name="Продукт")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    class Meta:
        verbose_name = "Заказанный продукт"  # Название модели в единственном числе
        verbose_name_plural = "Заказанные продукты"  # Название модели во множественном числе
        ordering = ('-order',)

    def __str__(self):
        return '{} {}'.format(self.id, self.product)

    # Метод get_cost() для получения общей стоимости позиции в корзине
    def get_cost(self):
        return self.price * self.quantity