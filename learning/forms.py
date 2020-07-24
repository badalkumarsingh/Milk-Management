from .models import Milk, Setting
from django.forms import ModelForm, CheckboxInput, IntegerField
from django import forms
class MilkForm(ModelForm):
    class Meta:
        model = Milk
        fields = ['milk_taken']
        widgets = {
            'milk_taken' : CheckboxInput(attrs={"onchange": "document.getElementById('submit').disabled = !this.checked;"}),   
        }

class SettingForm(ModelForm):
    class Meta:
        model = Setting
        fields = ['price']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }