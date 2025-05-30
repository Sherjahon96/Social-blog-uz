from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile
import re
from .models import BlogPost



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=4)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.fullmatch(r'\d{4,}', password):
            raise forms.ValidationError("Parol faqat raqamlardan iborat bo'lishi va kamida 4 ta raqamdan iborat bo'lishi kerak.")
        return password


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Foydalanuvchi nomi")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'phone']
