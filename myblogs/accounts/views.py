from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'user already exist'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1']    )
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,"accounts/signup.html",{"error":"password must match"})
    else:
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
