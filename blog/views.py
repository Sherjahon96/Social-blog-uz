from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Sum, F
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):

    popular_posts = BlogPost.objects.order_by('-views')[:5]
    # Top 3 eng ko'p o'qilgan postlar (BlogPost modelida 'views' maydoni mavjud deb hisoblaymiz)
    top_posts = BlogPost.objects.order_by('-views')[:3]

    # Top 3 mualliflar – blog_posts aliased orqali o'z postlari soni bo‘yicha
    top_authors = User.objects.annotate(num_posts=Count('blog_posts')).order_by('-num_posts')[:3]

    # Platforma statistikalari
    total_posts = BlogPost.objects.count()
    total_users = User.objects.count()
    total_views = BlogPost.objects.aggregate(total_views=Sum('views'))['total_views'] or 0

    context = {
        'popular_posts': popular_posts,
        'top_posts': top_posts,
        'top_authors': top_authors,
        'total_posts': total_posts,
        'total_users': total_users,
        'total_views': total_views,
    }
    return render(request, 'home.html', context)


# Boshqa view funksiyalari...
def blog_list(request):
    posts_list = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 5)  # har sahifada 5 ta post chiqsin
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, post_id):
    # Postni oling
    post = get_object_or_404(BlogPost, id=post_id)
    
    # Ko'rishlar sonini atomik ravishda oshiring
    BlogPost.objects.filter(id=post_id).update(views=F('views') + 1)
    
    # Yangilangan post ma'lumotlarini olish uchun (ixtiyoriy)
    post.refresh_from_db()  
    
    return render(request, 'blog/blog_detail.html', {'post': post})



def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.author != request.user:
        messages.error(request, "Siz faqat o‘zingiz yaratgan postni tahrirlashingiz mumkin!")
        return redirect('blog_list')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    # Faqat post egasi o'chira olishi mumkin
    if post.author != request.user:
        messages.error(request, "Siz faqat o'zingiz yaratgan postni o'chirishingiz mumkin!")
        return redirect('blog_list')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post muvaffaqiyatli o'chirildi!")
        # O'chirilganidan keyin foydalanuvchi o'z postlari sahifasiga yo'naltiriladi
        return redirect('my_posts')
    
    # Tasdiqlash sahifasini ko'rsatamiz
    return render(request, 'blog/confirm_delete.html', {'post': post})


@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})

def logout_view(request):
    logout(request)
    return redirect('home')

def bloggers_list(request):
    bloggers_list = User.objects.all()  # Agar keyinchalik reyting bo'yicha tartiblash kerak bo'lsa, annotate qo'llash mumkin
    paginator = Paginator(bloggers_list, 5)  # har sahifada 5 ta bloger
    page = request.GET.get('page')
    try:
        bloggers = paginator.page(page)
    except PageNotAnInteger:
        bloggers = paginator.page(1)
    except EmptyPage:
        bloggers = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/bloggers.html', {'bloggers': bloggers})

