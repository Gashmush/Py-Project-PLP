from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Profile
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=("email",)


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['photo']

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your username',
        'class':'px-6 py-4 w-full rounded-xl mb-2 '
    }))
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
                'placeholder':'Enter your password',
                'class':'px-6 py-4 w-full rounded-xl mb-2'

    }))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=["email","password1","password2"]
        
    email=forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder':'Enter your email',
            'class':'px-6 py-4 w-full rounded-xl mb-2'
        }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Enter your password',
            'class':'w-full px-6 py-4 rounded-xl mb-2',
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Repeat your password',
            'class':'w-full px-6 py-4 rounded-xl mb-2'
        }))