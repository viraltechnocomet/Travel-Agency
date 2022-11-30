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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {"demo":"value"}
        return render(request, self.template_name,context=context)
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        ...
        

class AddAdminView(TemplateView):
    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        init_data = {"type" : "ADMIN","created_by":user}
        form = SignUpForm(initial=init_data)
        
        context={
            'form': form
        }
        return render(request, "core/add-admin.html",context)
    @method_decorator(login_required)
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
    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        init_data = {"type" : "USER","created_by":user}
        form = SignUpForm(initial=init_data)
        print(form)
        context={
            'form': form
        }
        return render(request, "core/add-user.html", context)

    @method_decorator(login_required)
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
    @method_decorator(login_required)
    def get(self,request):
        if request.user.is_superuser:
            users = User.objects.filter(type="ADMIN")
        else:
            users = User.objects.filter(type="ADMIN").filter(created_by=request.user)
            
        context={
            "users" : users
        }
        return render(request, "core/list-all-admins.html",context)

    @method_decorator(login_required)
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
    @method_decorator(login_required)
    def get(self,request):
        if request.user.is_superuser:
            users = User.objects.filter(type="USER")
        else:
            users = User.objects.filter(type="USER").filter(created_by=request.user)
        context={
            "users" : users
        }
        return render(request, "core/list-all-users.html",context)

    @method_decorator(login_required)
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
    

@login_required(login_url='/')
def ItineraryView(request):
    
    context = {}
    if request.method=='POST':
        
        
        itinerary = ItineraryForms(request.POST,request.FILES)
        # img = ItineraryForms(request.POST, request.FILES)
        # img.data_image = request.FILES['data_image']
        
        # itinerary.data_image=img
        if itinerary.is_valid():
            itinerary.save()
            
            # print("hello...")
            # print(request.FILES)
            
            try: 
                cd = itinerary.cleaned_data
                img = Images(data_image=request.FILES['data_image'])
                img.save()
                

                pc = Itinerary(
                    # country = cd['country'],
                    # city = cd['city'],
                    # category_name = cd['category_name'],
                    # activity_name = cd['activity_name'],
                    image_id = img,
                    destination = cd['destination'],
                    description = cd['description'],
                    befor_you_go = cd['befor_you_go'],
                    nature = cd['nature'],
                    # season = cd['season'],
                    website = cd['website'],
                    link = cd['link'],
                    gps_cordinate = cd['gps_cordinate']
                )
                
                pc.save()
            
                messages.success(request, "Your data is successfully save......")
                print('Done.........')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")
        else:
            print(itinerary.errors)

    context['itinerary'] = ItineraryForms
    
    return render(request,'core/add-itinerary.html', context)

@login_required(login_url='/')           
def AddCountryView(request):
    context = {}

    if request.method == 'POST':
        form = AddCountryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data is successfully save......")
            return redirect('core:add-country')
        else:
            print("opps......")
    # else:
    #     form = AddCountryForm(request.POST)
    #     # messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                
    context['addcountry'] = AddCountryForm()
    return render(request, 'core/add-country.html', context)

@login_required(login_url='/')
def AddCityView(request):
    context = {}

    if request.method == 'POST':
        form = AddCityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data is successfully save......")
            return redirect('core:add-city')
        else:
            print("opps......")
    # else:
    #     messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                
    context['addcity'] = AddCityForm
    return render(request, 'core/add-city.html', context)

@login_required(login_url='/')
def AddCategoryView(request):
    context = {}

    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data is successfully save......")
            return redirect('core:add-category')
        else:
            print("opps......")
    # else:
    #     messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
            
    context['addcategory'] = AddCategoryForm
    return render(request, 'core/add-category.html', context)

@login_required(login_url='/')
def AddAgeView(request):
    context = {}

    if request.method == 'POST':
        form = AddAgeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data is successfully save......")
            return redirect('core:add-age')
        else:
            print("opps......")
    # else:
    #     messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
            
    context['addage'] = AddAgeForm
    return render(request, 'core/add-age.html', context)

@login_required(login_url='/')
def AddSeasonView(request):
    context = {}

    if request.method == 'POST':
        form = AddSeasonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data is successfully save......")
            return redirect('core:add-season')
        else:
            print("opps......")
    # else:
    #     messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
            
    context['addseason'] = AddSeasonForm
    return render(request, 'core/add-season.html', context)

@login_required(login_url='/')
def AddActivityView(request):
    context = {}

    if request.method == 'POST':
        form = AddActivityForm(request.POST)
        if form.is_valid():
            print("Done...")
            form.save()
            messages.success(request, "Your data is successfully save......")
            return redirect('core:add-activity')
        else:
            form = AddActivityForm(request.POST)
            print(form.errors)
            print("I'm So sorry......")
    # else:
    #     messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
            
    context['addactivity'] = AddActivityForm
    return render(request, 'core/add-activity.html', context)