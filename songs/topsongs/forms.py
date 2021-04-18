from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Playlist


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'placeholder': 'Username'}))

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'validate', 'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'validate', 'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'placeholder': 'Username'}))

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'validate', 'placeholder': 'Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class PlaylistCreationForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'validate', 'placeholder': 'Playlist Name'}))
    
    class Meta:
        model = Playlist
        fields = ['name']