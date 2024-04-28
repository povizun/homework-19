from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ContactsView, ProductDeleteView, ProductCreateView, \
    ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/', ProductDetailView.as_view(), name='view')
]
