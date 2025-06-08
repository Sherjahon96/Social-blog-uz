from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-language/', set_language, name='set_language'),
    path('', blog_views.home, name='home'),       # Bosh sahifa
    path('blog/', include('blog.urls')),          # Blog URL'lari
    path('accounts/', include('accounts.urls')),  # Accounts URL'lari
    #path('bloggers/', views.bloggers_list, name='bloggers_list'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
