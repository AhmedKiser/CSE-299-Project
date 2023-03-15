from django import forms
from django.core import validators
from .models import user
from django.forms import ModelForm




class userReg(ModelForm):
    class Meta:
        model = user
        fields = ('uName', 'uMail','uPhone','uDOB','uPassword')
        # name = forms.CharField()
        # email = forms.EmailField()
        # phone = forms.CharField()
        # DOB = forms.DateField()
        # password = forms.CharField(widget=forms.PasswordInput)
        # re_password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['uPassword']
        # wrongpass = self.cleaned_data['repassword']
        # if rightpass != wrongpass:
        #     raise forms.ValidationError('password not match')
