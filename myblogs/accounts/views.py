from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    return render(request,"accounts/signup.html")

def login(request):
    if request.method=='POST':
        auth.authenticate(username=request.POST['userId'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html',{"error":"username or password was wrong"})
    else:
        return render(request,"accounts/login.html")
def logout(request):
    #TODO:to be done later
    return render(request,"accounts/signup.html")
