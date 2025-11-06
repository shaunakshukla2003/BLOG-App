from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here

@login_required(login_url='')
def base(request):
    return render(request,'base.html')

def login_view(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user = User.objects.get(email=email)  
            if user.check_password(password):   
                auth_login(request, user)
                messages.success(request,'Login Successfully')
                return redirect('/')
            else:
                return HttpResponse("Wrong password")
        except User.DoesNotExist:
            return HttpResponse("No user with this email")
    
    
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        ename=request.POST.get('entername')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpass=request.POST.get('confirmpass')
        if password!=confirmpass:
            return redirect('signup')
            
        else:
            my_user=User.objects.create_user(ename,email,password)
            my_user.save()
            messages.success(request,'Account Created')
            return redirect('login') 
    return render(request,'signup.html')


def logout_view(request):
    auth_logout(request) 
    messages.success(request,'Logout Successfully') 
    return redirect('login')

