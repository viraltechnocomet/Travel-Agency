from django import forms
from django.forms import ModelForm

from accounts.models import CustomUser

from .models import *
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets

User = get_user_model()

class CreateUserCustomForm(ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        widgets = {
            # 'type':forms.HiddenInput(),
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
            'password':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"text",
                }
            ),
            
            # 'password2':forms.PasswordInput(
            #     attrs={
            #         'required' : True,
            #         'class':'form-control',
            #         'placeholder':"Confirm Password",
            #         'type':"text",
            #     }
            # ),
        }
               
class AddManagerForm(ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        widgets = {
            # 'type':forms.HiddenInput(),

            # 'image':forms.ImageField(),
            
            'first_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"First Name",
                    'type':"text",
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Last Name",
                    'type':"text",
                }
            ),
           'username':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"username",
                    'type':"text",
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"E-Mail",
                    'type':"text",
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"password",
                }
            ),
            # 'usertype':forms.ChoiceField(
            #     attrs={
            #         'required' : True,
            #         'class' : 'form-control',
            #         'type' : "dropdown",
            #     }
            # ),
            
        }
        
class AddAgentForm(ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        widgets = {
            'type':forms.HiddenInput(),
            
            'first_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"First Name",
                    'type':"text",
                }
            ),
            'last_name':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Last Name",
                    'type':"text",
                }
            ),
           'username':forms.TextInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"username",
                    'type':"text",
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"E-Mail",
                    'type':"text",
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'required' : True,
                    'class':'form-control',
                    'placeholder':"Password",
                    'type':"password",
                }
            ),
            
        }


    
    
        


        
