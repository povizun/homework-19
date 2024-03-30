from datetime import date

from django.db import models

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
    product_image = models.ImageField(verbose_name='превью товара', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateField(auto_now=True, verbose_name='ата последнего изменения (записи в БД)')

    manufactured_at = models.DateField(default=date.today, verbose_name='Дата производства продукта')

    def __str__(self):
        return f"{self.product_name}, {self.price} р."

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)
