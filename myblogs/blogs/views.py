from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
# Create your views here.
def home(request):
    return render(request,'blogs/home.html')

@login_required
def create(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['body']:
            blog=Blog()
            blog.title=request['title']
            blog.body=request['body']
    else:
        return render(request,"blogs/create.html")