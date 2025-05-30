from django.urls import path
from blog import views
from .views import blog_list, blog_detail, create_blog_post, edit_blog_post

urlpatterns = [
    path('', views.home, name='home'),  # Asosiy sahifa
    path('blog/', blog_list, name='blog_list'),  # Blog sahifasi
    path('blog/<int:post_id>/', blog_detail, name='blog_detail'),
    path('blog/create/', create_blog_post, name='create_blog_post'),
    path('blog/<int:post_id>/edit/', edit_blog_post, name='edit_blog_post'),
]

