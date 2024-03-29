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

    # choices_list=list(Itinerary.objects.all().values('id','destination','data_image'))
    # print(choices_list)
    # res = [(val["id"],val["destination"]) for key,val in enumerate(choices_list)]
    image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Package Name', 'type':"text",})))
    # details=forms.MultipleChoiceField(choices=res, widget=(forms.CheckboxSelectMultiple(attrs={'type':"checkbox",})))
    
    def save(self, commit=True):
        ...
        
class PackageUpadateForms(ModelForm):
    
    class Meta:
        model= Destinations
        fields = ('image', 'name')

    # choices_list=list(Itinerary.objects.all().values('id','destination'))
    # res = [(val["id"],val["destination"]) for key,val in enumerate(choices_list)]
    
    image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    name = forms.CharField(max_length = 150, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Package Name', 'type':"text",})))
    # details=forms.MultipleChoiceField(choices=res, widget=(forms.CheckboxSelectMultiple(attrs={'type':"checkbox",})))

   
    
class RatePackageForm(forms.ModelForm):
    
    class Meta:
        model = RatingDestination
        fields = ('rate',)
        
    rate=forms.ChoiceField(choices=RATE_CHOICES,widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select"})))
    
    
class RateAccommodationForm(forms.ModelForm):
    class Meta:
        model = RatingAccommodation
        fields = ('rate_ac',)
        
    rate_ac=forms.ChoiceField(choices=RATE_CHOICES,widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select"})))
    
        
class AccommodationForm(forms.Form):
    ac_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    ac_name = forms.CharField(max_length = 250, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Hotel Name', 'type':"text",})))
    destination = forms.ModelChoiceField(queryset=Destinations.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    country = forms.ModelChoiceField(queryset=Country.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    city = forms.ModelChoiceField(queryset=City.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    
class AccommodationUpdateForm(ModelForm):
    class Meta:
        model= Accommodation
        fields = '__all__'
        
    ac_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    ac_name = forms.CharField(max_length = 250, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Hotel Name', 'type':"text",})))
    destination = forms.ModelChoiceField(queryset=Destinations.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    country = forms.ModelChoiceField(queryset=Country.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    city = forms.ModelChoiceField(queryset=City.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
        
        
class TravelDocumentForm(forms.Form):
    ticket_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    ticket_info = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Ticket Info', 'type':"text", 'rows': 3, 'cols': 2}))
    reservation_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    reservation_info = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Reservation Info', 'type':"text", 'rows': 3, 'cols': 2}))
    
class TravelTicketUpdateForm(ModelForm):
    class Meta:
        model = TravelDocument
        fields = ('ticket_image', 'ticket_info')
        
    ticket_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    ticket_info = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Ticket Info', 'type':"text", 'rows': 3, 'cols': 2}))
    
class TravelReservationUpdateForm(ModelForm):
    class Meta:
        model = TravelDocument
        fields = ('reservation_image', 'reservation_info')
        
    reservation_image = forms.ImageField(widget=(forms.FileInput(attrs={'class': 'd-done', 'type': 'file',})))
    reservation_info = forms.CharField(widget=forms.Textarea(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Reservation Info', 'type':"text", 'rows': 3, 'cols': 2}))
    
class AddBucketForm(ModelForm):
    class Meta:
        model = Bucket
        fields = ('accommodation_id', 'client_number', 'start_journey_date', 'end_journey_date')

    accommodation_id = forms.ModelChoiceField(queryset=Accommodation.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    client_number = forms.CharField(max_length = 250, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Client Number', 'type':"text",})))
    start_journey_date = forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    end_journey_date = forms.DateField(widget=(forms.DateInput(attrs={'required' : True, 'class':'form-control', 'type':"date",})))
    
class LoyaltForm(ModelForm):
    class Meta:
        model = Loyalty
        fields = ('loyalty_value', 'user')
       
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all(),to_field_name="id", widget=(forms.Select(attrs={'required' : True, 'class':'form-control', 'type':"select",})))
    loyalty_value = forms.CharField(max_length = 250, widget=(forms.TextInput(attrs={'required' : True, 'class':'form-control', 'placeholder': 'Enter Loyalty Value', 'type':"text",})))