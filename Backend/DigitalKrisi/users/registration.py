from django import forms

class userReg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    DOB = forms.DateField()
    password = forms.PasswordInput()
