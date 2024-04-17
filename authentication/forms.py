<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
=======
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
>>>>>>> e2365ae11d1cbe8848e691bc074ce0d04e76e7b1


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
<<<<<<< HEAD
=======


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'email']
>>>>>>> e2365ae11d1cbe8848e691bc074ce0d04e76e7b1
