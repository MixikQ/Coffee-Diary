from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, PostCreationForm
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", { "posts": posts})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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
    data = { "profile": User.objects.get(id=id),
             "posts": Post.objects.filter(by_user = id) }
    return render(request, 'profile.html', data)

def edit_profile(request, id):
    return redirect('userpage', id=request.user.id)

def postpage(request, id):
    try:
        data = { "post": Post.objects.get(id=id) }
    except:
        return redirect('home')
    return render(request, 'postpage.html', data)

def create_post(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.by_user = request.user
            post.save()
            return redirect('post', id=post.id)
    else: 
        form = PostCreationForm()
    return render(request, 'create-post.html', {'form': form})

def edit_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return redirect('home')
    if post.by_user != request.user:
        return redirect('postpage', id=id)
    if request.method == "POST":
        form = PostCreationForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('postpage', id=post.id)
    else:
        form = PostCreationForm(instance=post)   
    data = { "post": post,
             "form": form }
    return render(request, 'edit-post.html', data)

def delete_post(request, id):
    try:
        if request.method == "POST":
            post = Post.objects.get(id=id)
            if request.user == post.by_user:
                Post.objects.get(id=post.id).delete()
                return redirect('userpage', id=post.by_user.id)
    except:
        return redirect('home')