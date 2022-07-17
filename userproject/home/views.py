from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user correct credential
        user = authenticate(username=username, password=password)
        print(username)
        print(password)
        if user is not None:
           auth_login(request,user)
           return redirect("/")
        else:
        #    print("fdb")
           return render(request,'login.html')
    return render(request,'login.html')


def logout(request):
    logout(request)
    return redirect("/login")