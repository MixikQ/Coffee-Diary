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