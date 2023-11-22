from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        
        email=request.POST['email']
        passw=request.POST['password']
        cpassw=request.POST['cpassword']
        if passw==cpassw:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email exists')
                return redirect(register)
            else:
                print("r")
                query=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],username=request.POST['uname'],email=email,password=passw)
                query.set_password(passw)
                query.save()
                return redirect(login)
        else:
            messages.info(request,"Both Passwords dont match")
            return redirect(register)
    return render(request,'register.html')
def login_user(request):
    if request.method=="POST":
        query=authenticate(request,username=request.POST['email'],password=request.POST['password'])
        if query is None:
            messages.error(request,"Invalid credentials")
            return redirect(login)
        else:
            login(request,query)
            return redirect(index)
    else:
        return render(request,'login.html')