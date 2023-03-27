from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin
from .models import prediction


# Create your views here.
def landingPage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def predict(request):
    if request.method=='POST':
        nt=request.POST.get('n')
        pp=request.POST.get('p')
        kp=request.POST.get('k')
        ph=request.POST.get('ph')

        new_data = prediction(n = nt, p = pp, k = kp, ph = ph)
        new_data.save()
    
    
    return render(request, 'prediction.html')
    


# def registration(request):
#     if request.method == 'POST':
#         fb = userReg(request.POST)
#         if fb.is_valid():
#             print(fb.cleaned_data['uPassword'])
#             # print(fb.cleaned_data['repassword'])
#             fb.save()
    
#     else:
#         fb = userReg()
#     return render(request,'registration.html',{'form': fb})

def registration(request):
    
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.success(request, 'Profile details updated.')
            return redirect('registration') 
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'registration.html')

def LoginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            authlogin(request,user)
            return redirect('registration')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



# def login(request):
#     if request.method == 'POST':
#         def my_view(request):
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('')
#             else:
#                 messages.success = (request,'error in log in ')
#                 return redirect('login.html')
#     else:
#         return render(request,'login.html',{})