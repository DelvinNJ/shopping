from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from accounts.views import *
from accounts import context_processors

# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            if 'register' in request.POST:
                username = request.POST['email']
                cpassword = request.POST['cpassword']
                first_name = request.POST['fname']
                last_name = request.POST['lname']
                if User.objects.filter(Q(username=username)|Q(email=email)).exists():
                    messages.warning(request, 'Email-id already taken')
                    return redirect('register')
                if password != cpassword:
                    messages.warning(request, 'Password does not match')
                    return redirect('register')
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Successfully register your account')
            if 'login' in request.POST:
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    messages.info(request,"Invalid username or password")
                    return redirect('register')
    return render(request,'user/register.html')


def Logout(request):
    logout(request)
    return redirect('register')



def grapes(request):
    return render(request,'user/grapes.html')