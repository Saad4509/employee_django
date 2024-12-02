from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # Add any additional fields or customization here
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']