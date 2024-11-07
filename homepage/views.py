from django.shortcuts import render

from authentication.models import UserProfile
from blog.models import BlogPost
# Create your views here.

def home(request):
    user_type = None  # Default user_type to None for unauthenticated users
    
    if request.user.is_authenticated:  # Check if the user is logged in
        try:
            user_profile = request.user.userprofile  # Attempt to access the UserProfile
            user_type = user_profile.user_type  # Get the user_type
        except UserProfile.DoesNotExist:
            user_type = None  # Handle the case where UserProfile doesn't exist

    context = {
        'user_type': user_type  # Pass the user_type to the template
    }
    return render(request, "homepage/index.html", context)

def index(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'blog_posts': blog_posts})