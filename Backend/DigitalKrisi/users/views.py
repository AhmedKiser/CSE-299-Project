from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin
from .models import prediction
from .forms import InputForm
import pickle
import numpy as np
import pandas as pd


model = pickle.load(open('C:/Users/User/Desktop/299/CSE-299-Project/Model/Linear_Reg.pkl', 'rb'))


# Create your views here.
def landingPage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def predict(request):
    
    if request.method=='POST':
        nt= int(request.POST.get('n'))
        pp= int(request.POST.get('p'))
        kp= int(request.POST.get('k'))
        ph= int(request.POST.get('ph'))
        

        # with open('C:/Users/User/Desktop/299/CSE-299-Project/Model/Linear_Reg.pkl','rb') as file: 
        #         model = pickle.load(file)
        # model = pickle.load(open('C:/Users/User/Desktop/299/CSE-299-Project/Model/Linear_Reg.sav', 'rb'))

        new = pickle.load(open("C:/Users/User/Desktop/299/CSE-299-Project/Model/Linear_Reg.pkl", "rb"))
        y = int ( new.predict([[nt,pp,kp,ph]]) )

        if y == 0:
            c = 'papaya'
        elif y == 1:
            c = 'orange'
        elif y == 2:
            c = 'orange'
        elif y == 3:
            c = 'muskmelon'
        elif y == 4:
            c = 'orange'
        elif y == 5:
            c = 'muskmelon'
        elif y == 6:
            c = 'orange'
        elif y == 7:
            c = 'muskmelon'
        elif y == 8:
            c = 'orange'
        elif y == 9:
            c = 'muskmelon'
        elif y == 10:
            c = 'orange'
        elif y == 11:
            c = 'muskmelon'
        elif y == 12:
            c = 'orange'
        elif y == 13:
            c = 'muskmelon'
        elif y == 14:
            c = 'orange'
        elif y == 15:
            c = 'muskmelon'
        elif y == 16:
            c = 'orange'
        elif y == 17:
            c = 'muskmelon'
        elif y == 18:
            c = 'orange'
        elif y == 19:
            c = 'muskmelon'
        elif y == 20:
            c = 'orange'
        elif y == 21:
            c = 'muskmelon'
        elif y == 22:
            c = 'orange'
        
        
        
        else:
            c = 'invalid'

        
        
        return render(request, 'prediction.html', {'result' : c})
    return render(request, 'prediction.html')
        
        
   


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": prediction.objects.all()}
    return render(request, "results.html", data)

# def predict(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             # Get the input values from the form
#             temperature = form.cleaned_data['temperature']
#             humidity = form.cleaned_data['humidity']
#             rainfall = form.cleaned_data['rainfall']

#             # Load the ML model
#             with open('model.pkl', 'rb') as f:
#                 model = pickle.load(f)

#             # Make a prediction using the model
#             prediction = model.predict(np.array([[temperature, humidity, rainfall]]))[0]

#             # Map the prediction index to the crop name
#             crop_names = ['wheat', 'rice', 'maize', 'chickpea', 'kidney beans', 'pigeon peas', 'moth beans', 'mung beans', 'black gram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
#             predicted_crop = crop_names[prediction]

#             # Render the result page
#             context = {'predicted_crop': predicted_crop}
#             return render(request, 'result.html', context)
#     else:
#         form = InputForm()
#     context = {'form': form}
#     return render(request, 'home.html', context)



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