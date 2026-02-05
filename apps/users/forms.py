from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "email"]


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "password1", "password2"]
