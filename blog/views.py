from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm  # Import your form
from authentication.models import UserProfile
from .models import BlogPost  # Import your model
import random


@login_required
def blog_form(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)  # Do not save yet
            user_profile = UserProfile.objects.get(user=request.user)  # Get UserProfile for the current user
            blog_post.author = user_profile  # Set the author to the UserProfile
            blog_post.save()  # Now save it to the database
            return redirect('index')  # Redirect to the index view after saving
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})


def index(request):
    # Get all blog posts and select 3 random ones
    blog_posts = BlogPost.objects.all()
    random_posts = random.sample(list(blog_posts), min(3, blog_posts.count()))  # Ensure we don't exceed available posts
    return render(request, 'index.html', {'random_posts': random_posts})
