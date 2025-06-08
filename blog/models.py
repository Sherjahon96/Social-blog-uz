from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)  # Yangi qo'shilgan maydon

    def __str__(self):
        return f"{self.title} - {self.author.username}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    # Ko'rishlar sonini oshiramiz
    BlogPost.objects.filter(id=post_id).update(views=F('views') + 1)
    # modelning yangilangan qiymatini olish uchun postni yangilash qayta oling
    post.refresh_from_db()
    return render(request, 'blog/blog_detail.html', {'post': post})
