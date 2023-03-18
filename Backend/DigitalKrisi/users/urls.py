from django.urls import path
from . import views


urlpatterns = [
    path('',views.landingPage, name="landing"),
     path('login/',views.LoginUser, name='login'),
     path('registration/',views.registration, name='registration'),
    
    
]