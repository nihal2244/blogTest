from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog,Comment
from django.utils import timezone
# Create your views here.


def home(request):
    blogs=Blog.objects
    
    return render(request, 'blogs/home.html',{'blogs':blogs})


@login_required(login_url="/accounts/login")
def create(request):
    if request.method == "POST":
        try:
            if request.POST['title'] and request.POST['body']:
                
                blog = Blog()
                blog.title = request.POST['title']
                blog.body = request.POST['body']
                blog.posted_on = timezone.datetime.now()
                blog.author = request.user
                
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
    comments=blog.comments.all()
    
    return render(request,"blogs/blog-page.html",{"blog":blog,"comments":comments} )

@login_required(login_url="/accounts/login")
def like(request,blog_id):
    if request.method=='POST':
        blog=get_object_or_404(Blog,pk=blog_id)
        blog.like_total+=1
        
        blog.save()

        return redirect("/blogs/" +str(blog.id))

def addComment(request,blog_id):
    article = get_object_or_404(Article,id = id)

    if request.method == "POST":
        comment_author = request.user
        comment_content = request.POST["comment_content"]

        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)

        newComment.article = article
        newComment.save()
    return redirect("/blogs/" +str(blog.id))