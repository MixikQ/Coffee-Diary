from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def user(request, id):
    data = {"id": id}
    return render(request, "user.html", context=data)

def post(request, id):
    data = {"id": id}
    return render(request, "post.html", context=data)