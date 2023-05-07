from django import forms

choices = (
("Брюки", "Брюки"),
("Джинсы", "Джинсы"),
("Куртки и тренчи", "Куртки и тренчи"),
("Обувь", "Обувь"),
("Платья", "Платья"),
("Сумки", "Сумки"),
("Худи", "Худи"),
("Топы", "Топы"),
("Футболки", "Футболки"),
("Шорты", "Шорты"),
("Юбки", "Юбки"),
("Показать всё", "Показать всё"),)


class CategoryForm(forms.Form):
    category = forms.TypedChoiceField(label="Категория", choices=choices, coerce=str, widget=forms.Select(attrs={'class': 'form-select', 'id': 'autoSizingSelect'}))







