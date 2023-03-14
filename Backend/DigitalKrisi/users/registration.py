from django import forms
from django.core import validators

class userReg(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    DOB = forms.DateField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['re_password']
        if rightpass != wrongpass:
            raise forms.ValidationError('password not match')
