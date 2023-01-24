from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()

admin.site.register(Itinerary)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Age)
admin.site.register(Season)
admin.site.register(Destinations)
admin.site.register(AddCartPackage)
