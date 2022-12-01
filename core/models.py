from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
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
    season=models.CharField(max_length=250, unique=True)
    
    def __str__(self):
        return self.season
    

class Images(models.Model):
    data_image=models.ImageField(upload_to='media/')
    # image_name=models.CharField(max_length=550, unique=True)
    
class Itinerary(models.Model):
    image_id=models.ForeignKey(Images,on_delete=models.CASCADE)
    destination = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    
    
    description=models.TextField()
    # budget=models.FloatField()
    befor_you_go=models.TextField()
    nature=models.CharField(max_length=250)
    website=models.CharField(max_length = 500)
    link=models.CharField(max_length=500)
    gps_cordinate=models.CharField(max_length=500)
    # spend_time=models.DateTimeField()
    # created_at=models.DateTimeField(auto_now_add=True)
    # update_at=models.DateTimeField(auto_now=True)
    
    
    
class Package(models.Model):
    package_name=models.CharField(max_length=250,unique=True)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    itinerary_id=models.ForeignKey(Itinerary,on_delete=models.CASCADE)
    activity_id=models.ForeignKey(Activity,on_delete=models.CASCADE)
    
class Selected_Package(models.Model):
    use_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    package_id=models.ForeignKey(Package,on_delete=models.CASCADE)
    person=models.IntegerField()
    costing=models.FloatField(max_length=100)
    arriaval_time=models.DateTimeField()
    
    