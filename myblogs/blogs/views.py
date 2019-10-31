from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone
# Create your views here.


def home(request):
    return render(request, 'blogs/home.html')


@login_required
def create(request):
    if request.method == "POST":
        try:
            if request.POST['title'] and request.POST['body']:
                print(request.POST['title'], request.POST['body'])
                blog = Blog()
                blog.title = request.POST['title']
                # print(blog.title)
                blog.body = request.POST['body']
                print(blog.body)
                blog.posted_on = timezone.datetime.now()
                blog.author = request.user
                print("author", blog.author)
                blog.save()
                return redirect("/blogs/" +str(blog.id))
            else:
                return render(request, "blogs/create.html", {"error": "Require all fields"})
        except Exception as e:
            print(error, e.message, e.args)

    else:
        return render(request, "blogs/create.html")

def blog_details(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,"blogs/blog-page.html",{"blog":blog} )
