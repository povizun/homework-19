# from datetime import date

from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='название категории')
    category_description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='название товара')
    product_description = models.TextField(verbose_name='описание товара')
    product_image = models.ImageField(upload_to='catalog/', verbose_name='превью товара', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateField(auto_now=True, verbose_name='ата последнего изменения (записи в БД)')

    creator = models.ForeignKey(User, verbose_name='Создатель', help_text='Укажите создателя товара', **NULLABLE,
                                on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')

    # manufactured_at = models.DateField(default=date.today, verbose_name='Дата производства продукта')

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)
        permissions = [
            ("can_edit_is_published", "Can edit is_published"),
            ("can_edit_category", "Can edit category"),
            ("can_edit_product_description", "Can edit product_description")
        ]


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='version', verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=50, verbose_name='Название версии')
    is_current_version = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    def __str__(self):
        return f"{self.version_name}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('product',)
