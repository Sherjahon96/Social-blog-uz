from django.urls import path
from .views import (
    home,
    blog_list,
    blog_detail,
    create_blog_post,
    edit_blog_post,
    delete_blog_post,
    my_posts,
    logout_view,
    bloggers_list,
)

urlpatterns = [
    path('', home, name='home'),  # Dashboard (bosh sahifa)
    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:post_id>/', blog_detail, name='blog_detail'),
    path('blog/create/', create_blog_post, name='create_blog_post'),
    path('blog/<int:post_id>/edit/', edit_blog_post, name='edit_blog_post'),
     path('blog/<int:post_id>/delete/', delete_blog_post, name='delete_blog_post'),
    path('bloggers/', bloggers_list, name='bloggers_list'),
    path('my-posts/', my_posts, name='my_posts'),
    path('logout/', logout_view, name='logout'),
]
