# Generated by Django 4.2 on 2023-04-30 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='Введите наименование категории', max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование предмета', max_length=60, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену предмета', max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение предмета', null=True, upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, help_text='Введите описание продукта', null=True, verbose_name='Описание продукта')),
                ('available', models.BooleanField(default=True, help_text='Введите статус наличия', verbose_name='В наличии')),
                ('category', models.ForeignKey(blank=True, help_text='Выберете категорию', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
    ]
