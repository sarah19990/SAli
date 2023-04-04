from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2','first_name','last_name']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateInput()
    class Meta:
        model = Profile
        fields = ['image','address','country','city','date_of_birth']