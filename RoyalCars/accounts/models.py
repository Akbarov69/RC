from django.db import models
from django import forms


class Loginform(forms.Form):
    username = forms.CharField(
        label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'password', 'id': 'password'}))


class SignForm(forms.Form):
    name = forms.CharField(label='First_name', max_length=20)
    sname = forms.CharField(label='Second_name', max_length=25)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_check = forms.CharField(label='Password(repeat)', widget=forms.PasswordInput)