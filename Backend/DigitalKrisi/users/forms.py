from django import forms

class InputForm(forms.Form):
    temperature = forms.FloatField(label='Temperature')
    humidity = forms.FloatField(label='Humidity')
    rainfall = forms.FloatField(label='Rainfall')
