from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your username'}))

class ResetForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Type your email'}))


class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Type your firstname'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Type your lastname'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Type your email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Type your username'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Type your password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Type your password again'}))