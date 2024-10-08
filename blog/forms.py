# forms.py
from django import forms
from blog.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']  # Specify the fields to include in the form
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),  # Use a textarea for the body field
        }
