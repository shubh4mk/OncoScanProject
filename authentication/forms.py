from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # User fields only

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    date_of_birth = forms.DateField(required=False)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=False)
    profile_picture = forms.ImageField(required=False)
    user_type = forms.ChoiceField(choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

    def save(self, commit=True):
        # Save User instance
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])  # Hash the password

        if commit:
            user.save()
            # Create or update the UserProfile instance
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'first_name': self.cleaned_data.get('first_name'),
                    'last_name': self.cleaned_data.get('last_name'),
                    'date_of_birth': self.cleaned_data.get('date_of_birth'),
                    'gender': self.cleaned_data.get('gender'),
                    'profile_picture': self.cleaned_data.get('profile_picture'),
                    'user_type': self.cleaned_data.get('user_type')
                }
            )
        return user
