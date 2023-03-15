from django.shortcuts import render
from .registration import userReg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .registration import userReg





# Create your views here.
def landingPage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def registration(request):
    if request.method == 'POST':
        fb = userReg(request.POST)
        if fb.is_valid():
            print(fb.cleaned_data['uPassword'])
            # print(fb.cleaned_data['repassword'])
            fb.save()
    
    else:
        fb = userReg()
    return render(request,'registration.html',{'form': fb})