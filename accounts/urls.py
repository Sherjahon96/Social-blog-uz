from django.urls import path
from . import views




urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_detail'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
