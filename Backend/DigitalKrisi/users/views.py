from django.shortcuts import render

from .registration import userReg




# Create your views here.
def landingPage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    fb = userReg()
    return render(request,'registration.html',{'form': fb})