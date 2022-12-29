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
     
class Itinerary(models.Model):
    data_image=models.ImageField(upload_to='media/', null=True, blank=True)
    destination = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=True, null=True)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    description=models.TextField()
    befor_you_go=models.TextField()
    nature=models.CharField(max_length=250)
    website=models.CharField(max_length = 500)
    link=models.CharField(max_length=500)
    gps_cordinate=models.CharField(max_length=500)
    phone_no=models.CharField(max_length=20, null=True)
    # spend_time=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.destination
    
    
class Package(models.Model):
    package_image=models.ImageField(upload_to='media/', null=True, blank=True)
    package_name=models.CharField(max_length=250,unique=True)
    itinerary_details=models.ManyToManyField(Itinerary, blank=True)
    from_date=models.DateField(blank=True,null=True)
    to_date=models.DateField(blank=True,null=True)
    price=models.CharField(max_length=250, null=True)
    days=models.CharField(max_length=250, null=True)
    nights=models.CharField(max_length=250, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.package_name   
    
class PackageCart(models.Model):
    Package_data=models.ForeignKey(Package, on_delete=models.CASCADE)
    
class AddCartPackage(models.Model):
    package_details=models.ForeignKey(Package,on_delete=models.CASCADE)
    itinerary_select=models.ManyToManyField(Itinerary, blank=True)
    start_date=models.DateField(blank=True,null=True)
    end_date=models.DateField(blank=True,null=True)
    adults=models.CharField(max_length=250,blank=True,null=True)
    children=models.CharField(max_length=250,blank=True,null=True)
    infant=models.CharField(max_length=250,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.package_details.package_name
    

class Selected_Package(models.Model):
    use_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    package_id=models.ForeignKey(Package,on_delete=models.CASCADE)
    person=models.IntegerField()
    costing=models.FloatField(max_length=100)
    arriaval_time=models.DateTimeField()
    
    