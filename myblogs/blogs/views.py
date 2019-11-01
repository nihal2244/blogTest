from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment,Likes
from django.utils import timezone

#dashboard view function 
def home(request):
    pass
    blogs = Blog.objects

    return render(request, 'blogs/home.html', {'blogs': blogs})

# creating new blog
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

                return redirect("/blogs/" + str(blog.id))
            else:
                return render(request, "blogs/create.html", {"error": "Require all fields"})
        except Exception as e:
            print(error, e.message, e.args)

    else:
        return render(request, "blogs/create.html")

# fetching blog filed and comments
def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = blog.comments.all()
    likes=blog.likes.all()
    blog.views_total += 1
    blog.save()
    return render(request, "blogs/blog-page.html", {"blog": blog, "comments": comments,"likes":likes})

# like incriment
@login_required(login_url="/accounts/login")
def like(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        liked_user=request.user
        print(liked_user)
        like_fil=Likes.objects.filter(pk=blog_id)
        if like_fil:                                                             # if the particular post is there
            if str(liked_user) not in str(like_fil):                                       # then we check the user which is us, in there
                like_obj = Likes(liked_author=liked_user,like=True)    #if we there and we returned this data, this part for saving data, I mean if this data is already created than we dont have to delete and create again, we just change LikeModel.liked true or false state, so that if you create like and it will never delete, it just change liked or like state
                like_obj.blog=blog
                like_obj.save()                                                      # if data is created then we say 'new'
    return redirect("/blogs/" + str(blog.id))


@login_required(login_url="/accounts/login")
def addComment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == "POST":
        comment_author = request.user
        print("yolo", request.POST)
        comment_content = request.POST["comments"]

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content)
        newComment.blog = blog
        newComment.save()
    return redirect("/blogs/" + str(blog.id))


