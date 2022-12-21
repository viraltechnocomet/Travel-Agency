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
    
 
]
