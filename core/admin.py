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
admin.site.register(Accomodation)

class TravelAdmin(admin.ModelAdmin):
    list_display = ["user"]
admin.site.register(TravelDocument, TravelAdmin)

class RateAdmin(admin.ModelAdmin):
    list_display = ["user", "destination_id", "rate"]
admin.site.register(Rating, RateAdmin)


