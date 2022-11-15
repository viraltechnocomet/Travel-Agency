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
               

class CourntryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"
        
        widgets = {
            'country':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'city':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"City",
                    'type':"text",
                }
            ),
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
        widgets = {
            'category_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
        }
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        
        widgets = {
            'Activity_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
        }
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"
        
        widgets = {
            'image_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'data_image':forms.FileInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"img",
                }
            ),
        }
        
class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = "__all__"
        
        widgets = {
            'image_id':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'description':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'budget':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'befor_you_go':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'nature':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'season':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'website':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'link':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'gps_cordinate':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'spend_time':forms.DateTimeBaseInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"date",
                }
            ),
            'created_at':forms.DateTimeBaseInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"date",
                }
            ),
            'update_at':forms.DateTimeBaseInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"date",
                }
            ),
        }
        
class PackageForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = "__all__"
        
        widgets = {
            'package_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'package_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'itinerary_id':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'activity_id':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
        }
        
class Selected_Package(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = "__all__"
        
        widgets = {
            'use_id':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'package_id':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'person':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'costing':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"text",
                }
            ),
            'arriaval_time':forms.DateTimeBaseInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Country",
                    'type':"date",
                }
            ),
        }
        


    
    
        


        
