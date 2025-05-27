from django.shortcuts import render
from .models import Post
from .models import BlogPost, Author  # Blog va mualliflarni olish uchun modellardan foydalanish

def home_view(request):
    blogs = BlogPost.objects.all()[:5]  # Oxirgi 5 blog
    authors = Author.objects.all()[:5]  # Eng mashhur 5 muallif
    return render(request, 'home.html', {'blogs': blogs, 'authors': authors})
