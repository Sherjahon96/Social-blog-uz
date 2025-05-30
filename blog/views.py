
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm

@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if post.author != request.user:  # Tekshiramiz: faqat post egasi tahrir qilishi mumkin
        messages.error(request, "Siz faqat o‘zingiz yaratgan blog postni tahrirlashingiz mumkin!")
        return redirect('blog_list')  # Asosiy blog sahifasiga qaytariladi

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post.id)  # Yangilangan post sahifasiga qaytish
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})



def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Muallifni qo‘shish
            post.save()
            return redirect('blog_list')  # Yangi post yaratilgandan keyin ro‘yxatga qaytish
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_post.html', {'form': form})


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Eng yangi postlarni chiqarish
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})



def home(request):
    return render(request, 'home.html')
