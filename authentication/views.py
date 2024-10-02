from django.forms import ValidationError
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')

        # Basic validation
        if password1 != password2:
            messages.error(request, _("Passwords do not match."))
            return render(request, 'authentication/signup.html')

        try:
            # Create the user
            user = User.objects.create_user(
                username=username,
                password=password1,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            # Create the user profile
            profile = UserProfile.objects.create(user=user, user_type=user_type)

            # Optionally, save the profile picture if provided
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()

            messages.success(request, _("Successfully signed up! You can now log in."))
            return redirect('signin')  # Redirect to the signin page

        except ValidationError as e:
            messages.error(request, _("Error creating account: ") + str(e))

    return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change 'homepage' to your desired URL after login
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    
    return render(request, 'authentication/signin.html') 


@login_required
def signout(request):
    auth_logout(request)  # Log out the user
    messages.success(request, "You have been logged out successfully.")
    return redirect('home') 
