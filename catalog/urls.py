from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ContactsView, ProductDeleteView, ProductCreateView, \
    ProductUpdateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('categories/', CategoryListView.as_view(), name='categories')
]
