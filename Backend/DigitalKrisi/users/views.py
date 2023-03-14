from django.shortcuts import render

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
            print(fb.cleaned_data['password'])
            print(fb.cleaned_data['re_password'])
    
    else:
        fb = userReg()
    return render(request,'registration.html',{'form': fb})