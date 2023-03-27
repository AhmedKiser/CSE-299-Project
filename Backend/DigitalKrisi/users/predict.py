from django import forms
from django.core import validators
from .models import prediction
from django.forms import ModelForm




class userReg(ModelForm):
    class Meta:
        model = prediction
        fields = ('n', 'p','k','ph')
     