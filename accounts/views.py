from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def RegisterAdmin(request):
    if request.method=='POST':
        username=request.POST['u']
        password1=request.POST['p1']
        password2=request.POST['p2']
        email=request.POST['e']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('/')
            else:
                user=User.objects.create_user(email=email,username=username,password=password1)                
                return redirect('Login')            
        else:
            messages.info(request, 'passwords are not matching')
            return redirect('/')
        
    return render(request,'Register.html')

def Login(request):
    if request.method=='POST':
        username=request.POST['u']
        password=request.POST['p1']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)

            print(user)
            return redirect('home')
        else:
            messages.warning(request, 'check your credentials again!!!') 
            return redirect('Login')
    return render(request,'Login.html')

def Logout(request):
    auth.logout(request)
    return redirect('Login')