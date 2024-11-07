from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import random

from blog.models import BlogPost

# Import BlogPostForm here
from .forms import BlogPostForm

@login_required
def blog_form(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assign the current user as author
            blog_post.save()
            return redirect('home')  # Redirect to index view
    else:
        form = BlogPostForm()

    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_user(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assign the current user as author
            blog_post.save()
            return redirect('home')  # Redirect to index view
    else:
        form = BlogPostForm()

    return render(request, 'blog/blog_user.html', {'form': form})

def index(request):
    blog_posts = BlogPost.objects.all()
    random_posts = random.sample(list(blog_posts), min(3, blog_posts.count())) 
    return render(request, 'home', {'random_posts': random_posts})
