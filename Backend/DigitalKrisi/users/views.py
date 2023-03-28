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




# Create your views here.
def landingPage(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def predict(request):
    
    if request.method=='POST':
        nt=float(request.POST.get('n'))
        pp=float(request.POST.get('p'))
        kp=float(request.POST.get('k'))
        ph=float(request.POST.get('ph'))

        # with open('C:/Users/User/Desktop/299/CSE-299-Project/Model/model_pickle','rb') as file: 
        #         model = pickle.load(file)
        # # model = pickle.load(open('C:/Users/User/Desktop/299/CSE-299-Project/Model/Linear_Reg.sav', 'rb'))
        
        # prediction = model.predict(np.array([[nt, pp, kp, ph]]))[0]
        # # prediction = model.predict([[nt, pp, kp, ph]])
        
        # # new_data = prediction(n = nt, p = pp, k = kp, ph = ph)
        # # new_data.save()
        # crop_names = ['wheat', 'rice', 'maize', 'chickpea', 'kidney beans', 'pigeon peas', 'moth beans', 'mung beans', 'black gram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']
        # predicted_crop = crop_names[prediction]
        # context = {'predicted_crop': predicted_crop}
        # return render(request, 'result.html', context)


        model = pd.read_pickle(r"C:\Users\User\Desktop\299\CSE-299-Project\Model\modelpickle")
        # Make prediction
        result = model.predict([[nt ,pp, kp, ph]])

        classification = result[0]

        prediction.objects.create(n = np, p = pp, k = kp, ph=ph)
    
    return JsonResponse({'result': classification, 'n': np,
                             'p': kp, 'k': pp, 'ph': ph},
                            safe=False)


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