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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    

class SelectDestinations(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    destination_id = models.CharField(max_length=225, blank=True, null=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    name = models.CharField(max_length=250,unique=True)
    details = models.ManyToManyField(Itinerary, blank=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
class Accommodation(models.Model):
    ac_image = models.ImageField(upload_to='media/', null=True, blank=True)
    ac_name = models.CharField(max_length=225, blank=True, null=True)
    destination=models.ForeignKey(Destinations,on_delete=models.CASCADE,blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ac_name 
    
class Bucket(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    destination_id = models.ForeignKey(Destinations,on_delete=models.CASCADE)
    accommodation_id = models.ForeignKey(Accommodation,on_delete=models.CASCADE, blank=True, null=True)
    client_number = models.CharField(max_length=500, blank=True, null=True)
    start_journey_date = models.DateField(blank=True, null=True)
    end_journey_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username + " " + self.destination_id.name
       
RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]     
      
class RatingDestination(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    destination_id = models.ForeignKey(Destinations,on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + " " + self.destination_id.name
    
class RatingAccommodation(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    accommodation_id = models.ForeignKey(Accommodation,on_delete=models.CASCADE)
    rate_ac = models.PositiveSmallIntegerField(choices=RATE_CHOICES, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
class TravelDocument(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    ticket_image = models.ImageField(upload_to='media/', null=True, blank=True)
    ticket_info = models.CharField(max_length=500, blank=True, null=True)
    reservation_image = models.ImageField(upload_to='media/', null=True, blank=True)
    reservation_info = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Loyalty(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='user_loyalty')
    # itinerary_id = models.ForeignKey(Itinerary, on_delete=models.CASCADE, blank=True, null=True)
    loyalty_value = models.CharField(max_length=225, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username + " " + self.loyalty_value
       
