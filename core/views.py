from http.client import HTTPResponse
from django.views.generic import (
    TemplateView,
    DetailView,
    View,
    ListView,
    DetailView,
)

from django.http import (
    JsonResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
    HttpResponse
)
from django.shortcuts import (
    render,redirect
)

from accounts.models import CustomUser
from django.conf import settings
import os
from accounts.forms import SignUpForm
from core.forms import *


from django.core import files
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from templates import *
from django.contrib import messages
from accounts.models import USER_TYPES

from django.contrib.auth import get_user_model

User = get_user_model()

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"

class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo":"value"}
        return render(request, self.template_name,context=context)

    def post(self, request, *args, **kwargs):
        ...
        


class AddAdminView(TemplateView):
    def get(self,request):
        user = request.user
        init_data = {"type" : "ADMIN","created_by":user}
        form = SignUpForm(initial=init_data)
        
        context={
            'form': form
        }
        return render(request, "core/add-admin.html",context)

    def post(self,request):
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            # return redirect(request, "app/dashboard.html")
            return redirect('core:add-admin')
        else:
            messages.error(request, form.errors)

        context={
            'form': form
        }
        return render(request, "core/add-admin.html",context)

class AddUserView(TemplateView):
    def get(self,request):
        user = request.user
        init_data = {"type" : "USER","created_by":user}
        form = SignUpForm(initial=init_data)
        print(form)
        context={
            'form': form
        }
        return render(request, "core/add-user.html", context)

    def post(self,request):
        form = SignUpForm(data = request.POST)
        print(form)
        if form.is_valid():
            form.save()
            # return redirect(request, "app/dashboard.html")
            return redirect('core:add-user')
        else:
            messages.error(request, form.errors)

        context={
            'form': form
        }
        return render(request, "core/add-user.html",context)

class ListAllAdminView(TemplateView):
    def get(self,request):
        if request.user.is_superuser:
            users = User.objects.filter(type="ADMIN")
        else:
            users = User.objects.filter(type="ADMIN").filter(created_by=request.user)
            
        context={
            "users" : users
        }
        return render(request, "core/list-all-admins.html",context)

    def post(self,request):
        action = request.POST.get("action")
        user_id = request.POST.get("user_id")
        user = User.objects.filter(id=user_id)[0]
        print("action",action,
        "user_id",user_id,
        )
        if action == "active":
            messages.success(request, f"{user} activated succssfully")
            user.is_active = True
        elif action == "active":
            messages.success(request, f"{user} De-activated succssfully")
            user.is_active = False
        elif action == "edit":
            form = SignUpForm(instance = user)
            context={
                'form': form
            }
            redirect_str = f"/edit-admin/{user_id}"
            return redirect(redirect_str)
        if action == "delete":
            user.delete()
            messages.success(request, f"{user} deleted succssfully")
        if request.user.is_superuser:
            users = User.objects.filter(type="ADMIN")
        else:
            users = User.objects.filter(type="ADMIN").filter(created_by=request.user)
        context={
            "users" : users
        }
        return render(request, "core/list-all-admins.html",context)

class ListAllUsersView(TemplateView):
    def get(self,request):
        if request.user.is_superuser:
            users = User.objects.filter(type="USER")
        else:
            users = User.objects.filter(type="USER").filter(created_by=request.user)
        context={
            "users" : users
        }
        return render(request, "core/list-all-users.html",context)

    def post(self,request):
        action = request.POST.get("action")
        user_id = request.POST.get("user_id")
        user = User.objects.filter(id=user_id)[0]

        if action == "active":
            messages.success(request, f"{user} activated succssfully")
            user.is_active = True

        if action == "edit":
            form = SignUpForm(instance = user)
            context={
                'form': form
            }
            redirect_str = f"/edit-user/{user_id}"
            return redirect(redirect_str)
        if action == "delete":
            user.delete()
            messages.success(request, f"{user} deleted succssfully")
        users = User.objects.filter(type="USER")
        context={
            "users" : users
        }
        return render(request, "core/list-all-users.html",{context})
    


def ItineraryView(request):
    
    context = {}
    if request.method=='POST':
        
        itinerary = ItineraryForms(request.POST)
        print(itinerary)
        if itinerary.is_valid():
            countryid=request.POST.get('country')
            country=Country.objects.get(country=countryid)
            
            cityid=request.POST.get('city')
            city=City.objects.get(city=cityid)
            
            categoryid=request.POST.get('category_name')
            category=City.objects.get(category_name=categoryid)
            
            ageid=request.POST.get('age')
            age=Age.objects.get(age=ageid)
            
            seasonid=request.POST.get('season')
            season=Season.objects.get(season=seasonid)
            
            try:
                itinerary.country=country
                itinerary.city=city
                itinerary.category_name=category
                itinerary.age=age
                itinerary.season=season
                
                
                itinerary.save()
                messages.success(request, "Your data is successfully save......")
                print('Done.........')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")
        # else:
        #     print(itinerary.errors)

    context['itinerary'] = ItineraryForms
    
    return render(request,'core/add-itinerary.html', context)

def AddCountryView(request):
    context = {}

    if request.method == 'POST':
        form = AddCountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:add-country')
    else:
        print("opps......")
            
    context['addcountry'] = AddCountryForm
    return render(request, 'core/add-country.html', context)

def AddCityView(request):
    context = {}

    if request.method == 'POST':
        form = AddCityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:add-city')
    else:
        print("opps......")
            
    context['addcity'] = AddCityForm
    return render(request, 'core/add-city.html', context)

def AddCategoryView(request):
    context = {}

    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:add-category')
    else:
        print("opps......")
            
    context['addcategory'] = AddCategoryForm
    return render(request, 'core/add-category.html', context)

def AddAgeView(request):
    context = {}

    if request.method == 'POST':
        form = AddAgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:add-age')
    else:
        print("opps......")
            
    context['addage'] = AddAgeForm
    return render(request, 'core/add-age.html', context)

def AddSeasonView(request):
    context = {}

    if request.method == 'POST':
        form = AddSeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:add-season')
    else:
        print("opps......")
            
    context['addseason'] = AddSeasonForm
    return render(request, 'core/add-season.html', context)