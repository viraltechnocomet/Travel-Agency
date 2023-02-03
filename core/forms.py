from django import forms
from django.forms import ModelForm

from accounts.models import CustomUser

from core.models import *
from django.contrib.auth import get_user_model
from django.contrib.admin import widgets
from core.models import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm




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
        
class UpdateUserCustomForm(ModelForm):
    class Meta:
        model = User

        fields = ('username', 'email')

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
        }
        
class AddCountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
    country = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control','placeholder': 'Country...', 'type':"text",})))
    
class AddCityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
    city = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control','placeholder': 'City...', 'type':"text",})))
    
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    category_name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control','placeholder': 'Category...', 'type':"text",})))
      
class AddAgeForm(ModelForm):
    class Meta:
        model = Age
        fields = '__all__'
    age = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control','placeholder': 'Age...', 'type':"text",})))
    
class AddSeasonForm(ModelForm):
    class Meta:
        model = Season
        fields = '__all__'
    season = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control','placeholder': 'Season...', 'type':"text",})))
  
class AddActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
    activity_name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control','placeholder': 'Activity...', 'type':"text",})))

class ItineraryForms(forms.Form):
    
    data_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    destination = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Destination Name', 'type':"text",})))
    country=forms.ModelChoiceField(queryset=Country.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    city=forms.ModelChoiceField(queryset=City.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    category_name = forms.ModelChoiceField(queryset=Category.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    activity_name = forms.ModelChoiceField(queryset=Activity.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    age=forms.ModelChoiceField(queryset=Age.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    description = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Description', 'type':"text", 'rows': 3, 'cols': 2}))
    befor_you_go=forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Before You Go', 'type':"text", 'rows': 3, 'cols': 2}))
    nature=forms.CharField(max_length=150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Nature', 'type':"text",})))
    season=forms.ModelChoiceField(queryset=Season.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    website=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Website', 'type':"text",})))
    link=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Link', 'type':"text",})))
    gps_cordinate=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'GPS Cordinate', 'type':"text",})))
    phone_no=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Phone No', 'type':"text",})))
    budget=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Amount', 'type':"text",})))

    
    def save(self, commit=True):
        ...
        
class ItineraryUpdateForms(ModelForm):
    
    class Meta:
        model= Itinerary
        fields = '__all__'
    
    data_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    destination = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Destination Name', 'type':"text",})))
    country=forms.ModelChoiceField(queryset=Country.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    city=forms.ModelChoiceField(queryset=City.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    category_name = forms.ModelChoiceField(queryset=Category.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    activity_name = forms.ModelChoiceField(queryset=Activity.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    age=forms.ModelChoiceField(queryset=Age.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    description = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Description', 'type':"text", 'rows': 3, 'cols': 2}))
    befor_you_go=forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Before You Go', 'type':"text", 'rows': 3, 'cols': 2}))
    nature=forms.CharField(max_length=150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Nature', 'type':"text",})))
    season=forms.ModelChoiceField(queryset=Season.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    website=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Website', 'type':"text",})))
    link=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Link', 'type':"text",})))
    gps_cordinate=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'GPS Cordinate', 'type':"text",})))
    phone_no=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Phone No', 'type':"text",})))
    budget=forms.CharField(max_length=500, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Amount', 'type':"text",})))

        

class ItineraryPackageForms(forms.Form):

    choices_list=list(Itinerary.objects.all().values('id','destination'))
    res = [(val["id"],val["destination"]) for key,val in enumerate(choices_list)]
    
    image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Package Name', 'type':"text",})))
    # days = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Days', 'type':"text",})))
    # nights = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Nights', 'type':"text",})))
    details=forms.MultipleChoiceField(choices=res, widget=(forms.SelectMultiple(attrs={'required' : True, 'class':'form-control', 'type':"select",'name':"itinarary_choices"})))
    # from_date=forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    # to_date=forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    # price=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Price', 'type':"text",})))
    
    def save(self, commit=True):
        ...
        
class PackageUpadateForms(ModelForm):
    
    class Meta:
        model= Destinations
        fields = '__all__'

    choices_list=list(Itinerary.objects.all().values('id','destination'))
    res = [(val["id"],val["destination"]) for key,val in enumerate(choices_list)]
    
    image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Package Name', 'type':"text",})))
    # days = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Days', 'type':"text",})))
    # nights = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Nights', 'type':"text",})))
    details=forms.MultipleChoiceField(choices=res, widget=(forms.SelectMultiple(attrs={'required' : True, 'class':'form-control', 'type':"select",'name':"itinarary_choices"})))
    # from_date=forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    # to_date=forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    # price=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Price', 'type':"text",})))


class AddCartForm(ModelForm):

    CHOICES = {}
    class Meta:
        model= AddCartPackage
        fields = '__all__'
         
    # package_name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Package Name', 'type':"text",})))

    start_date=forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    end_date=forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    adults=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Adults', 'type':"text",})))
    children=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Children', 'type':"text",})))
    infant=forms.CharField(max_length=550, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Infant', 'type':"text",})))
    # itinerary_datas=forms.MultipleChoiceField(choices=CHOICES, widget=(forms.CheckboxSelectMultiple(attrs={'required' : True, 'type':"checkbox",})))
    
class RateForm(forms.ModelForm):
    
    rate=forms.ChoiceField(choices=RATE_CHOICES,widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select"})))

    class Meta:
        model = Rating
        fields = ('rate',)