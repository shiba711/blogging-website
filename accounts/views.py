import re
from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_user(request):
    if request.method == "POST":

        username= request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print("Logged In")
        else:
            print("User Does Not Exist")
            return redirect('/accounts/signup/')
            
        return redirect('/blog/allblogs')

    else:
        return render (request,'accounts/login.html')

def signup(request):
    if request.method == "POST":
        username= request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        password = request.POST["password"]

        newuser = User(username=username,first_name=firstname, last_name=lastname)
        newuser.set_password(password)
        newuser.save()

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print("Logged In")
        else:
            print("User Does Not Exist")


        return redirect('/blog/allblogs/')

    elif request.method == "GET":
        return render(request,'accounts/signup.html')

def home(request):
    return render (request,'accounts/home.html')

#def logout_user(request):
#   logout(request)
#    return redirect(request,'/blog/allblogs/')
def logout_user(request):
    logout(request)

    return redirect('/accounts/home/')