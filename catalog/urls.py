from django.urls import path

from catalog.views import ProductDetailView, ProductListView, ContactsView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view())
]
