from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', {'form': form})

def profile(request, id):
    data = { "user": User.objects.get(id=id),
             "posts": Post.objects.filter(by_user = id) }
    return render(request, 'profile.html', data)

def profile_redirect(request):
    id = request.user.id
    if id is not None:
        return redirect('userpage', id = id)
    return redirect('login')