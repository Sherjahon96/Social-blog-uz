"""
URL configuration for socialblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Test uchun view
from django.conf import settings
from django.conf.urls.static import static
from blog_app.views import home_view  # Home sahifa uchun funksiya import

# Asosiy sahifa view funksiyasi
def home_view(request):
    return HttpResponse("Asosiy sahifa ishlayapti!")  # Test uchun asosiy sahifa

# Test sahifa view funksiyasi
def test_view(request):
    return HttpResponse("Test sahifa ishlayapti!")  # Test uchun sahifa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Bosh sahifa
    path('blog/', include('blog_app.urls')),  # Blog sahifasi
    path('accounts/', include('accounts.urls')),  # Foydalanuvchi hisoblari uchun URL'lar
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

