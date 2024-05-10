from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_current_version' and field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


    # def clean_is_active(self):
    #     is_active = self.cleaned_data.get('is_active')
    #     if is_active and Version.objects.filter(is_active=True, product=self.cleaned_data.get('product')).exists():
    #         raise ValidationError('Только одна активная версия')
    #     return is_active


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_image', 'category', 'price',)

    @staticmethod
    def check_words(data):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in data.lower():
                raise forms.ValidationError('Нельзя создавать продукты с запрещенными словами в названии и описании')

        return data

    def clean_product_name(self):
        cleaned_data = self.check_words(self.cleaned_data['product_name'])

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.check_words(self.cleaned_data['product_description'])

        return cleaned_data


class ProductModeratorForm(ProductForm):
    class Meta:
        model = Product
        fields = ('product_description', 'category', 'is_published',)


class ProductModeratorCreatorForm(ProductForm):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description', 'product_image', 'category', 'price', 'is_published',)
