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
admin.site.register(Accommodation)

class TravelAdmin(admin.ModelAdmin):
    list_display = ["user"]
admin.site.register(TravelDocument, TravelAdmin)

class RatePackageAdmin(admin.ModelAdmin):
    list_display = ["user", "destination_id", "rate"]
admin.site.register(RatingDestination, RatePackageAdmin)

class RateAccommodationAdmin(admin.ModelAdmin):
    list_display = ["user", "accommodation_id", "rate_ac"]
admin.site.register(RatingAccommodation, RateAccommodationAdmin)

class ConformPackageAdmin(admin.ModelAdmin):
    list_display = ["user", "destination_id", "accommodation_id"]
admin.site.register(Bucket, ConformPackageAdmin)

class LoyaltyAdmin(admin.ModelAdmin):
    list_display = ["user", "loyalty_value"]
admin.site.register(Loyalty, LoyaltyAdmin)


