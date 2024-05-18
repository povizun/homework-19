from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, CreateView, DeleteView
from django.forms import inlineformset_factory

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm, ProductModeratorCreatorForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories_from_cache


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        version = {}
        for product in context_data.get('object_list'):
            version[product.pk] = (product.version.filter(is_current_version=True).first())
        context_data['active_version'] = version

        return context_data


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_categories_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        user = self.request.user
        self.object.creator = user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        is_moderator = user.has_perm("catalog.can_edit_is_published") and user.has_perm("catalog.can_edit_category") and user.has_perm("catalog.can_edit_product_description")
        if is_moderator and user == self.object.creator:
            return ProductModeratorCreatorForm
        elif is_moderator:
            return ProductModeratorForm
        elif user == self.object.creator:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
