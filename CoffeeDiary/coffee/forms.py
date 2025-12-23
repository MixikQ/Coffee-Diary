from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    
class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "recipe", "comment"]
        
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите текущий пароль'
        }),
        label="Текущий пароль"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите новый пароль'
        }),
        label="Новый пароль"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите новый пароль'
        }),
        label="Подтверждение пароля"
    )
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
