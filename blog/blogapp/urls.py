from django.urls import path
from .views import BlogListView, BlogDetailView, About

app_name = 'blogapp'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),]