from django import forms
from django.forms import ModelForm

from accounts.models import CustomUser

from .models import *
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets
from core.models import *

User = get_user_model()


class CreateUserCustomForm(ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        widgets = {
            'type':forms.HiddenInput(),
            'username':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"UserName",
                    'type':"text",
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"E-Mail",
                    'type':"text",
                }
            ),
            'password1':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"text",
                }
            ),
            
            'password2':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Confirm Password",
                    'type':"text",
                }
            ),
        }
        
class ItineraryForms(forms.Form):
    # data_image = forms.FileField(upload_to='media', height_field=None, width_field=None, max_length=100)
    data_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'form-control', 'type': 'file',})))
    image_name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Destination Name', 'type':"text",})))
    country = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Country Name', 'type':"text",})))
    city = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'City Name', 'type':"text",})))
    category_name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Category', 'type':"text",})))
    activity_name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Activity Name', 'type':"text",})))
    age=forms.IntegerField(widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Age', 'type':"text",})))
    description = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Destination Name', 'type':"text", 'rows': 3, 'cols': 2}))
    befor_you_go=forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Destination Name', 'type':"text", 'rows': 3, 'cols': 2}))
    nature=forms.CharField(max_length=150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Nature', 'type':"text",})))
    season=forms.CharField(max_length=150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Season', 'type':"text",})))
    website=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Website', 'type':"text",})))
    link=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Link', 'type':"text",})))
    gps_cordinate=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'GPS Cordinate', 'type':"text",})))
    
   
    
    
    
    
    
    
    
    

    
    
        


        
