from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    """The class how defind the the all params for user register"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
