from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.home, name='home'),       # Bosh sahifa
    path('blog/', include('blog.urls')),          # Blog URL'lari
    path('accounts/', include('accounts.urls')),  # Accounts URL'lari
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
