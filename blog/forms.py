from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavha kiriting'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Maqola matnini kiriting'}),
        }
