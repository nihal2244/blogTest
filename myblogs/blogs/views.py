from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request,'blogs/home.html')

@login_required
def create(request):
    if request.method=="POST":    
        if request.POST['title'] and request.POST['body']:
            blog=Blog()
            blog.title=request.POST['title']
            # print(blog.title)
            blog.body=request.POST['body']
            print(blog.body)
            blog.created_date=timezone.datetime.now()
            blog.author=request.user
            
            return redirect('home')
        else:
            return render(request,"blogs/create.html",{"error":"Require all fields"})

    else:
        return render(request,"blogs/create.html")