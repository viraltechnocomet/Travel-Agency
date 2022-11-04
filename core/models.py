from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
# from accounts import models

User = get_user_model()

class Country(models.Model):
    country = models.CharField(max_length=60, unique=True)
    city = models.CharField(max_length=60, unique=True)
    
class Category(models.Model):
    c_name = models.CharField(max_length=255, unique=True)
    
class Activity(models.Model):
    activity_name = models.CharField(max_length=160, unique=True)
