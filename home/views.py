from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
# Create your views here.
@login_required(login_url="/login")
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        
        email=request.POST['email']
        passw=request.POST['password']
        cpassw=request.POST['cpassword']
        username=request.POST['uname']
        if passw==cpassw:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=request.POST['uname']).exists():
                messages.info(request,'User name or Email exists')
                return redirect(register)
            else:
                print("r")
                query=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],username=username,email=email,password=passw)
                query.set_password(passw)
                query.save()
                return redirect(login)
        else:
            messages.info(request,"Both Passwords dont match")
            return redirect(register)
    return render(request,'register.html')
def login_user(request):
    if request.method=="POST":
        uname=request.POST['email']
        password=request.POST['password']
        query=authenticate(request,username=uname,password=password)
        if query is None:
            messages.error(request,"Invalid credentials")
            return redirect(login_user)
        else:
            login(request,query)
            return render(request,'index.html',{"uname":uname})
    else:
        return render(request,'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')
@login_required(login_url='/login')
def secondpage(request):
    return render(request,'second.html')