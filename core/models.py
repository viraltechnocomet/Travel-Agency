from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.contrib.postgres.fields import ArrayField
# from accounts import models

User = get_user_model()

class Country(models.Model):
    country = models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return self.country
    
    
class City(models.Model):
    city = models.CharField(max_length=60, unique=True)
    
    def __str__(self):
        return self.city
    
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.category_name
    
class Activity(models.Model):
    activity_name = models.CharField(max_length=160, unique=True)
    
    def __str__(self):
        return self.activity_name
    
class Age(models.Model):
    age = models.CharField(max_length=160, unique=True)
    
    def __str__(self):
        return self.age
    
class Season(models.Model):
    season = models.CharField(max_length=250, unique=True)
    
    def __str__(self):
        return self.season
     
class Itinerary(models.Model):
    data_image = models.ImageField(upload_to='media/', null=True, blank=True)
    destination = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    befor_you_go = models.TextField()
    nature = models.CharField(max_length=250)
    website = models.CharField(max_length = 500)
    link = models.CharField(max_length=500)
    gps_cordinate = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=20, null=True)
    budget = models.CharField(max_length=10, blank=True, null=True)
    
    # spend_time=models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.destination
    
class Destinations(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    name = models.CharField(max_length=250,unique=True)
    details = models.ManyToManyField(Itinerary, blank=True)
    # from_date = models.DateField(blank=True,null=True)
    # to_date = models.DateField(blank=True,null=True)
    # price = models.CharField(max_length=250, null=True)
    # days = models.CharField(max_length=250, null=True)
    # nights = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name   
    
class AddCartPackage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    itinerary_cart = models.ManyToManyField(Itinerary,blank=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    adults = models.CharField(max_length=250,blank=True,null=True)
    children = models.CharField(max_length=250,blank=True,null=True)
    infant = models.CharField(max_length=250,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Accomodation(models.Model):
    ac_image = models.ImageField(upload_to='media/', null=True, blank=True)
    ac_name = models.CharField(max_length=225, blank=True, null=True)
    destination=models.ForeignKey(Destinations,on_delete=models.CASCADE,blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.ac_name 
    
class Confirmed_Package(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    package_id = models.ForeignKey(Destinations,on_delete=models.CASCADE)
    accomodation_id = models.ForeignKey(Accomodation,on_delete=models.CASCADE, blank=True, null=True)
    client_number = models.CharField(max_length=500, blank=True, null=True)
    start_ac_date = models.DateField(blank=True, null=True)
    end_ac_date = models.DateField(blank=True, null=True)
    
    
RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]     
      
class Rating(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    destination_id = models.ForeignKey(Destinations,on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " " + self.destination_id.name
    
# class Loyalty(models.Model):
#     l_value = models.CharField(max_length=225, blank=True, null=True)
       
class TravelDocument(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    ticket_image = models.ImageField(upload_to='media/', null=True, blank=True)
    ticket_info = models.CharField(max_length=500, blank=True, null=True)
    reseration_proof_image = models.ImageField(upload_to='media/', null=True, blank=True)
    reservation_info = models.CharField(max_length=500, blank=True, null=True)
    
# selected packages -> all the selected todo list will be appeared to admin and they can assign the loyalty point to that selected todo list in place of money.