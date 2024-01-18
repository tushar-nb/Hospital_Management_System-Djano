# from imaplib import _Authenticator
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'home/index.html')

def loginuser(request):
    if request.method=="POST" :
        username = request.POST.get('username') #check if user entered correct crediential
        password = request.POST.get('password')
        # print(username,password)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else :
            return render(request,'home/login.html')
    return render(request,'home/login.html')
       

def logoutuser(request):
    logout(request)
    # return render(request,'logout.html')
    return redirect('/login')

