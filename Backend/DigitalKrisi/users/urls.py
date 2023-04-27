from django.urls import path
from . import views


urlpatterns = [
     path('',views.landingPage, name="landing"),
     path('login/',views.LoginUser, name='login'),
     path('about/',views.aboutus, name='about'),
     path('registration/',views.registration, name='registration'),
     path('predict/',views.predict, name="predict"),
     path('classf/',views.classf),
     path('classf/',views.classf,name='classf'),
     
    
    
]