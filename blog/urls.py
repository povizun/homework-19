from django.urls import path

from blog.views import BlogPostDetailView, BlogPostListView, BlogPostDeleteView, BlogPostCreateView, BlogPostUpdateView
from blog.apps import BlogConfig
app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='index'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogPostUpdateView.as_view(), name='update'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='view')
]
