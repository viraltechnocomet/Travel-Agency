from django.contrib import admin
from django.urls import path,reverse_lazy,include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    # path('', RedirectView.as_view(url=reverse_lazy('accounts:login'))),
    # path('', views.DashboardView.as_view(), name='index'),
    path('dashboard/', views.DashboardView.as_view(),name='dashboard'),
    path('add-admin/', views.AddAdminView.as_view(), name='add-admin'),
    path('add-user/',views.AddUserView.as_view(), name='add-user'),
    path('list-all-admin/',views.ListAllAdminView.as_view(), name='list-all-admin'),
    path('list-all-users/',views.ListAllUsersView.as_view(), name='list-all-users'),
    path('update-admin/<int:id>/',views.UpdateAdmin, name='update-admin'),
    path('update-user/<int:id>/',views.UpdateUser, name='update-user'),
    
    
    path('add-itinerary/',views.ItineraryView, name='add-itinerary'),
    path('add-country/',views.AddCountryView, name='add-country'),
    path('add-city/',views.AddCityView, name='add-city'),
    path('add-category/',views.AddCategoryView, name='add-category'),
    path('add-age/',views.AddAgeView, name='add-age'),
    path('add-season/',views.AddSeasonView, name='add-season'),
    path('add-activity/',views.AddActivityView, name='add-activity'),
    path('itinerary', views.itineraryRead, name='itinerary'),
    path('itinerary-details/<int:id>/', views.itinerary_details, name='itinerary-details'),
    path('itinerary-delete/<int:id>/', views.ItineraryDelete, name='itinerary-delete'),
    path('itinerary-update/<int:id>/', views.ItineraryUpdate, name='itinerary-update'),
    path('add-itinerary-package/', views.ItineraryPackageView, name='add-itinerary-package'),
    path('package/', views.PackageRead, name='package'),
    path('package-details/<int:id>', views.PackageDetails, name='package-details'),
    path('package-delete/<int:id>/', views.PackageDelete, name='package-delete'),
    path('package-update/<int:id>/', views.PackageUpdate, name='package-update'),
    path('select-itinerary/<int:id>/', views.SelectItinerary, name='select-itinerary'),
    path('add-itineraries/', views.AddItinerary, name='add-itineraries'),
    path('remove-itineraries/', views.RemoveItinerary, name='remove-itineraries'),
    path('add-itineraries-user/', views.AddSelectDestinationForUser, name='add-itineraries-user'),
    path('select-itinerary-user/<int:id>/', views.SelectItineraryForUser, name='select-itinerary-user'),
    path('add-itineraries-for-user/', views.AddItineraryForUser, name='add-itineraries-for-user'),
    path('remove-itineraries-for-user/', views.RemoveItineraryForUser, name='remove-itineraries-for-user'),
    
    path('rate-package/<int:id>', views.RatePackage, name='rate-package'),
    path('rate-accommodation/<int:id>', views.RateAccommodation, name='rate-accommodation'),
    path('add-accommodation/', views.AccommodationView, name='add-accommodation'),
    path('accommodation/', views.AccommodationRead, name='accommodation'),
    path('accommodation-delete/<int:id>', views.AccommodationDelete, name='accommodation-delete'),
    path('accommodation-update/<int:id>/', views.AccommodationUpdate, name='accommodation-update'),
    path('add-travel-document/', views.TravelDocumentView, name='add-travel-document'),
    path('travel-document/', views.TravelDocumentRead, name='travel-document'),
    path('travel-document-delete/<int:id>/', views.TravelDocumentDelete, name='travel-document-delete'),
    path('travel-ticket-update/<int:id>/', views.TravelTicketUpdate, name='travel-ticket-update'),
    path('travel-reservation-update/<int:id>/', views.TravelReservationUpdate, name='travel-reservation-update'),
    path('add-bucket/<int:id>', views.AddBucketView, name='add-bucket'),
    path('bucket/', views.BucketView, name='bucket'),
    path('bucket-details/<int:id>', views.BucketDetails, name='bucket-details'),
    path('bucket-delete/<int:id>/', views.BucketDelete, name='bucket-delete'),
    path('bucket-update/<int:id>/', views.BucketUpdate, name='bucket-update'),
    path('add-loyalty/', views.LoyaltyView, name='add-loyalty'),
    path('loyalty/', views.LoyaltyRead, name='loyalty'),
    path('loyalty-delete/<int:id>/', views.LoyaltyDelete, name='loyalty-delete'),
    path('loyalty-update/<int:id>/', views.LoyaltyUpdate, name='loyalty-update'),
    
]
