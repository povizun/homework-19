from catalog.models import Product, Category

import json

from django.core.management import BaseCommand

from config.settings import BASE_DIR


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():

        categories_to_add = []
        with open(BASE_DIR / 'fixtures/catalog_data.json', "r") as file:
            data = json.load(file)
        for item in data:
            if item["model"] == "catalog.category":
                categories_to_add.append(item)
        return categories_to_add

    @staticmethod
    def json_read_products():
        products_to_add = []
        with open(BASE_DIR / 'fixtures/catalog_data.json', "r") as file:
            data = json.load(file)
        for item in data:
            if item["model"] == "catalog.product":
                products_to_add.append(item)
        return products_to_add

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category["pk"], category_name=category["fields"]["category_name"],
                         category_description=category["fields"]["category_description"])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product["pk"], product_name=product["fields"]["product_name"],
                        product_description=product["fields"]["product_description"],
                        product_image=product["fields"]["product_image"],
                        # получаем категорию из базы данных для корректной связки объектов
                        category=Category.objects.get(pk=product["fields"]["category"]),
                        price=product["fields"]["price"],
                        created_at=product["fields"]["created_at"],
                        updated_at=product["fields"]["updated_at"])
            )

        Product.objects.bulk_create(product_for_create)
