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
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator

from django.db.models import Q 

from django.core import files
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from templates import *
from django.contrib import messages
from accounts.models import USER_TYPES

from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model

import pdb

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
        
        user = request.user
        init_data = {"type" : "ADMIN","created_by":user}
        form = SignUpForm(data = request.POST, initial=init_data) 
        print(init_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin Added Successfully...")
            # return redirect(request, "app/dashboard.html")
            return redirect('core:list-all-admin')
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
        context={
            'form': form
        }
        return render(request, "core/add-user.html", context)

    @method_decorator(login_required)
    def post(self,request):
        user = request.user
        init_data = {"type" : "USER","created_by":user}
        form = SignUpForm(data = request.POST, initial=init_data)
        print(init_data)
        if form.is_valid():
            form.save()
            # return redirect(request, "app/dashboard.html")
            messages.success(request, "User Added Successfully...")
            return redirect('core:list-all-users')
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
            users = User.objects.filter(type="ADMIN")
            
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
            users = User.objects.filter(type="USER")
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
        return render(request, "core/list-all-users.html",context)
 
@login_required(login_url='/')   
def UpdateAdmin(request,id):
    
    context = {}
    
    if request.method == 'POST':
        Update_admin= CustomUser.objects.get(pk=id)
        update_admin_form = UpdateUserCustomForm(request.POST, instance=Update_admin)
        if update_admin_form.is_valid():
            print("Done...")
            update_admin_form.save()
            messages.success(request, "Admin SuccuessFully Updated")
            return redirect('core:list-all-admin')
        else:
            messages.error(request, update_admin_form.errors)
        context['update_admin_form'] = update_admin_form
        context['Update_admin'] = Update_admin
    else:
        Update_admin= CustomUser.objects.get(pk=id)
        print(Update_admin)
        update_admin_form = UpdateUserCustomForm(instance=Update_admin)
        print(update_admin_form)
        
        context['update_admin_form'] = update_admin_form
        context['Update_admin'] = Update_admin
    
    return render(request, 'core/update-admin.html', context)

@login_required(login_url='/')   
def UpdateUser(request,id):
    
    context = {}
    
    if request.method == 'POST':
        Update_user= CustomUser.objects.get(pk=id)
        update_user_form = UpdateUserCustomForm(request.POST, instance=Update_user)
        if update_user_form.is_valid():
            print("Done...")
            
            update_user_form.save()
            messages.success(request, "User SuccuessFully Updated")
            return redirect('core:list-all-users')
        else:
            messages.error(request, update_user_form.errors)
        context['update_user_form'] = update_user_form
        context['Update_user'] = Update_user
    else:
        Update_user= CustomUser.objects.get(pk=id)
        
        update_user_form = UpdateUserCustomForm(instance=Update_user)
        
        context['update_user_form'] = update_user_form
        context['Update_user'] = Update_user
    
    return render(request, 'core/update-user.html', context)   

@login_required(login_url='/')
def ItineraryView(request):
    
    context = {}
    if request.method=='POST':
        
        itinerary = ItineraryForms(request.POST,request.FILES)
        
        if itinerary.is_valid():
            itinerary.save()
            
            try: 
                cd = itinerary.cleaned_data
            
                pc = Itinerary(
                    data_image = request.FILES['data_image'],
                    country = cd['country'],
                    city = cd['city'],
                    category_name = cd['category_name'],
                    activity_name = cd['activity_name'],
                    age = cd['age'],
                    season = cd['season'],
                    destination = cd['destination'],
                    description = cd['description'],
                    befor_you_go = cd['befor_you_go'],
                    nature = cd['nature'],
                    website = cd['website'],
                    link = cd['link'],
                    gps_cordinate = cd['gps_cordinate'],
                    phone_no = cd['phone_no'],
                    budget = cd['budget'],
                )
                
                pc.save()
                
                messages.success(request, "Destination is created successfully......")
                print('Done.........')
                return redirect('core:itinerary')
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
            messages.success(request, "Country is created successfully......")
            return redirect('core:add-itinerary')
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
            messages.success(request, "City is created successfully......")
            return redirect('core:add-itinerary')
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
            messages.success(request, "Category is created successfully......")
            return redirect('core:add-itinerary')
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
            messages.success(request, "Age is created successfully......")
            return redirect('core:add-itinerary')
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
            messages.success(request, "Season is created successfully......")
            return redirect('core:add-itinerary')
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
            messages.success(request, "Activity is created successfully......")
            return redirect('core:add-itinerary')
        else:
            form = AddActivityForm(request.POST)
            print(form.errors)
            print("I'm So sorry......")
    # else:
    #     messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
            
    context['addactivity'] = AddActivityForm
    return render(request, 'core/add-activity.html', context)

@login_required(login_url='/')
def itineraryRead(request):
    context = {}
    
    if 'q' in request.GET:
        q = request.GET['q']
        itinerary = Itinerary.objects.filter(destination__icontains=q)
        print(itinerary)
    else:
        itinerary = Itinerary.objects.all().order_by("-created_at")

    context['itinerary'] = itinerary
    
    return render(request, 'core/itinerary.html', context)    

@login_required(login_url='/')
def itinerary_details(request, id):
    if request.method == "GET":
        context = {}
        itinerary_data = Itinerary.objects.get(pk=id)
        season_data = Season.objects.all()
        country_data = Country.objects.all()
        city_data = City.objects.all()
        activity_data = Activity.objects.all()
        age_data = Age.objects.all()
        
        context['itinerary_data'] = itinerary_data
        context['season_data'] = season_data
        context['country_data'] = country_data
        context['city_data'] = city_data
        context['activity_data'] = activity_data
        context['age_data'] = age_data
    
        return render(request, 'core/itinerary-details.html', context)
    else:
        return HttpResponse("Page not supported")

@login_required(login_url='/')
def ItineraryDelete(request, id):
    itinerary_data = Itinerary.objects.get(pk=id)
    if itinerary_data.delete():
        messages.success(request, 'Destination is SuccessFully Deleted....')
        return redirect('core:itinerary')
    else:
        messages.error(request, "Something wen't to delete Itinerary" )
    
    return render(request, 'core/itinerary.html', {'itinerary_data': itinerary_data})

@login_required(login_url='/')
def ItineraryUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        itinerary_datas = Itinerary.objects.get(pk=id)
        form = ItineraryUpdateForms(request.POST, request.FILES, instance=itinerary_datas)
        if form.is_valid():
            print("Done...")
            form.save()
            messages.success(request, "Destination is SuccuessFully Updated....")
            return redirect('core:itinerary')
        context['forms_data'] = form
        context['itinerary_datas'] = itinerary_datas
    else:
        itinerary_datas = Itinerary.objects.get(pk=id)
        
        form = ItineraryUpdateForms(instance=itinerary_datas)
        
        context['forms_data'] = form
        context['itinerary_datas'] = itinerary_datas
    
    return render(request, 'core/itinerary-update.html', context)


@login_required(login_url='/')
def ItineraryPackageView(request):
    
    context = {}
    iti = Itinerary.objects.all()
    if request.method=='POST':
        itineraries = request.POST.getlist("details")
        print(itineraries)

        obj_itineraries = list(Itinerary.objects.filter(pk__in = itineraries))
        print(obj_itineraries)
        
        package = ItineraryPackageForms(request.POST,request.FILES)
        
        if package.is_valid():
            package.save()
            
            try: 
                cd = package.cleaned_data
            
                pc = Destinations(
                    
                    image = request.FILES['image'],
                    name = cd['name'],
                )
                pc.save()
                pc.details.set(obj_itineraries)
                # print(pc.pk)
                
                messages.success(request, "Itinerary is created successfully......")
                print('Done.........')
                return redirect('core:package')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")
        else:
            print(package.errors)

    context['package'] = ItineraryPackageForms
    context['iti'] = iti
    
    return render(request,'core/add-itinerary-package.html', context)

@login_required(login_url='/')
def PackageRead(request):
    context = {}
    if 'q' in request.GET:
        q = request.GET['q']
        package = Destinations.objects.filter(name__icontains=q)
    else:
        package = Destinations.objects.all().order_by("-created_at")

    context['packages'] = package
    
    return render(request, 'core/package.html', context)

@login_required(login_url='/')
def PackageDetails(request, id):
    if request.method == "GET":
        context = {}
        
        package_datas = Destinations.objects.get(pk=id)
        package_itinerary_datas= package_datas.details.all()
        print(package_itinerary_datas)
        
        context['package_datas'] = package_datas
        context['package_itinerary_datas'] = package_itinerary_datas
    
        return render(request, 'core/package-details.html', context)
    else:
        return HttpResponse("Page not supported")

@login_required(login_url='/')
def PackageDelete(request, id):
    package_datas = Destinations.objects.get(pk=id)
    if package_datas.delete():
        messages.success(request, 'Itinerary is SuccessFully Deleted....')
        return redirect('core:package')
    else:
        messages.error(request, "Something wen't to delete Package" )
    
    return render(request, 'core/package.html', {'package_datas': package_datas})

@login_required(login_url='/')
def PackageUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        package_datas = Destinations.objects.get(pk=id)
        form = PackageUpadateForms(request.POST, request.FILES, instance=package_datas)
        if form.is_valid():
            form.save()
            messages.success(request, "Itinerary is SuccuessFully Updated....")
            return redirect('core:package')
        context['forms'] = form
        context['package_datas'] = package_datas
    else:
        package_datas = Destinations.objects.get(pk=id)
        
        form = PackageUpadateForms(instance=package_datas)
        
        context['forms'] = form
        context['package_datas'] = package_datas
    
    return render(request, 'core/package-update.html', context)

@login_required(login_url='/')
def SelectItinerary(request, id):
    context = {}
    if 'q' in request.GET:
        q = request.GET['q']
        package_datas = Destinations.objects.get(pk=id)
        package_itinerary_datas= package_datas.details.all()
        itinerary_data = Itinerary.objects.filter(destination__icontains=q)
        print(itinerary_data)
    else:
        package_datas = Destinations.objects.get(pk=id)
        package_itinerary_datas= package_datas.details.all()
        itinerary_data = Itinerary.objects.all()
        print(itinerary_data)
   
    context['package_datas'] = package_datas    
    context['itinerary_data'] = itinerary_data
    context['package_itinerary_datas'] = package_itinerary_datas
    return render(request, 'core/select-itinerary.html', context)

@login_required(login_url='/')
def AddItinerary(request):
    context={}
    if request.method=='POST':
        # pdb.set_trace()
        destination_id=request.POST.get('pkg_id')
        details=request.POST.get('iti_id')
        
        it_details = Itinerary.objects.filter(pk__in=details)
        print(it_details)
        destination=Destinations.objects.get(id=destination_id)
        print(destination)

        for it in it_details:
            destination.details.add(it)
        destination.save()
        
        messages.success(request,'Itinerary Is Successfully Add....')
        return redirect('core:select-itinerary', id=destination_id)
    return render(request, 'core/select-itinerary.html', context)


@login_required(login_url='/')
def RemoveItinerary(request):
    context={}
    if request.method=='POST':
        # pdb.set_trace()
        destination_id=request.POST.get('pkg_id')
        details=request.POST.get('iti_id')
        
        it_details = Itinerary.objects.filter(pk__in=details)
        print(it_details)
        destination=Destinations.objects.get(id=destination_id)
        print(destination)

        for it in it_details:
            destination.details.remove(it)
        destination.save()
        
        messages.success(request,'Itinerary Is Successfully Remove....')
        return redirect('core:select-itinerary', id=destination_id)
    return render(request, 'core/select-itinerary.html', context)


@login_required(login_url='/')
def SelectItineraryForUser(request, id):
    context = {}
    if 'q' in request.GET:
        q = request.GET['q']
        package_datas = Destinations.objects.get(pk=id)
        package_itinerary_datas= package_datas.details.all()
        itinerary_data = Itinerary.objects.filter(destination__icontains=q)

    else:
        package_datas = SelectDestinations.objects.get(pk=id)
        print(package_datas)
        package_itinerary_datas= package_datas.details.all()
        itinerary_data = Itinerary.objects.all()
   
    context['package_datas'] = package_datas    
    context['itinerary_data'] = itinerary_data
    context['package_itinerary_datas'] = package_itinerary_datas
    return render(request, 'core/select-itinerary-user.html', context)


@login_required(login_url='/')
def AddSelectDestinationForUser(request):
    context={}

    if request.method=='POST':
        user=request.POST.get('user_id')
        image=request.POST.get('image')
        name=request.POST.get('name')
        destination_id=request.POST.get('packag_id')   
        details=request.POST.getlist('itinerary_id')
        
        if SelectDestinations.objects.filter(destination_id=destination_id).exists():
            return redirect('core:add-bucket', id=destination_id)
        else:
            user = CustomUser.objects.get(id=user)
            destination=SelectDestinations(
                destination_id=destination_id,
                user=user,
                image=image,
                name=name,
            )
            destination.save()
            # destination.details.set(details)
            for it in details:
                print(it)
                destination.details.add(it)
            
            messages.success(request,'Success....')
            return redirect('core:add-bucket', id=destination_id)

    return render(request, 'core/select-itinerary.html', context)

@login_required(login_url='/')
def AddItineraryForUser(request):
    context={}
    if request.method=='POST':

        destination_id=request.POST.get('pkg_id')
        details=request.POST.get('iti_id')
        
        it_details = Itinerary.objects.filter(pk__in=details)
        print(it_details)
        destination=SelectDestinations.objects.get(id=destination_id)
        print(destination)

        for it in it_details:
            destination.details.add(it)
        destination.save()
        
        messages.success(request,'Itinerary Is Successfully Add....')
        return redirect('core:select-itinerary-user', id=destination_id)
    return render(request, 'core/select-itinerary.html', context)

@login_required(login_url='/')
def RemoveItineraryForUser(request):
    context={}
    if request.method=='POST':

        destination_id=request.POST.get('pkg_id')
        details=request.POST.get('iti_id')
        
        it_details = Itinerary.objects.filter(pk__in=details)
        print(it_details)
        destination=SelectDestinations.objects.get(id=destination_id)
        print(destination)

        for it in it_details:
            destination.details.remove(it)
        destination.save()
        
        messages.success(request,'Itinerary Is Successfully Remove....')
        return redirect('core:select-itinerary-user', id=destination_id)
    return render(request, 'core/select-itinerary.html', context)

@login_required(login_url='/')
def RatePackage(request,id):
    context = {}
    destination_id=Destinations.objects.get(pk=id)
    user=request.user
    if request.method == 'POST':
        rate_form=RatePackageForm(request.POST)
        print(rate_form)
        if rate_form.is_valid():
            rate=rate_form.save(commit=False)
            rate.user_id=user.id
            rate.destination_id=destination_id
            rate.save()
            messages.success(request, "Rating Are Successfully Given To " + destination_id.name)
            print('Done.........')
            return redirect('core:package')
    context['rate_form'] = RatePackageForm
    context['des'] = destination_id
    return render(request, 'core/rate-package.html',context)

@login_required(login_url='/')
def RateAccommodation(request,id):
    context = {}
    accommodation_id=Accommodation.objects.get(pk=id)
    user=request.user
    if request.method == 'POST':
        acr_form=RateAccommodationForm(request.POST)
        print(acr_form)
        if acr_form.is_valid():
            rate=acr_form.save(commit=False)
            rate.user_id=user.id
            rate.accommodation_id=accommodation_id
            rate.save()
            messages.success(request, "Rating Are Successfully Given To " + accommodation_id.ac_name)
            print('Done.........')
            return redirect('core:accommodation')
    context['acr_form'] = RateAccommodationForm
    context['accr'] = accommodation_id
    return render(request, 'core/rate-accommodation.html',context)

@login_required(login_url='/')
def AccommodationView(request):
    
    context = {}
    if request.method=='POST':
        
        accommodation = AccommodationForm(request.POST,request.FILES)
        
        if accommodation.is_valid():
            # accommodation.save()
            try: 
                cd = accommodation.cleaned_data
            
                pc = Accommodation(
                   
                    ac_image = request.FILES['ac_image'],
                    ac_name = cd['ac_name'],
                    destination = cd['destination'],
                    country = cd['country'],
                    city = cd['city'],
                    
                )
                pc.save()
                
                messages.success(request, "Your Accommodation is created successfully......")
                print('Done.........')
                return redirect('core:accommodation')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")
        else:
            print(accommodation.errors)

    context['accommodation'] = AccommodationForm
    
    return render(request,'core/add-accommodation.html', context)

@login_required(login_url='/')
def AccommodationRead(request):
    context = {}
    acc = Accommodation.objects.all().values_list('id')
    if 'q' in request.GET:
        q = request.GET['q']
        acc = Accommodation.objects.filter(ac_name__icontains=q)
    else:
        acc = Accommodation.objects.all().order_by("id")

    context['acc'] = acc
    return render(request, 'core/accommodation.html', context)

@login_required(login_url='/')
def AccommodationDelete(request, id):
    accomodation_data = Accommodation.objects.get(id=id)
    if accomodation_data.delete():
        messages.success(request, 'Accommodation is SuccessFully Deleted....')
        return redirect("core:accommodation")
    else:
        messages.error(request, "Something wen't wrong" )
        
    return render(request, 'core/accommodation.html', {'accomondation_data': accomodation_data})

@login_required(login_url='/')
def AccommodationUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        accommodation_datas = Accommodation.objects.get(pk=id)
        ac_form = AccommodationUpdateForm(request.POST, request.FILES, instance=accommodation_datas)
        if ac_form.is_valid():
            print("Done...")
            ac_form.save()
            messages.success(request, "Accommodation is SuccuessFully Updated....")
            return redirect('core:accommodation')
        context['ac_form'] = ac_form
        context['accommodation_datas'] = accommodation_datas
    else:
        accommodation_datas = Accommodation.objects.get(pk=id)
        
        ac_form = AccommodationUpdateForm(instance=accommodation_datas)
        
        context['ac_form'] = ac_form
        context['accommodation_datas'] = accommodation_datas
    
    return render(request, 'core/accommodation-update.html', context)

@login_required(login_url='/')
def TravelDocumentView(request):
    
    context = {}
    if request.method=='POST':
        
        traveldocument = TravelDocumentForm(request.POST,request.FILES)
        user=request.user
        
        if traveldocument.is_valid():
            
            try: 
                cd = traveldocument.cleaned_data    
            
                pc = TravelDocument(
                   
                    ticket_image = request.FILES['ticket_image'],
                    ticket_info = cd['ticket_info'],
                    reservation_image = request.FILES['reservation_image'],
                    reservation_info = cd['reservation_info'],
                )
                pc.user_id=user.id
                pc.save()

                messages.success(request, "Your Document is Upload successfully......")
                print('Done.........')
                return redirect('core:travel-document')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")
        else:
            print(traveldocument.errors)

    context['traveldocument'] = TravelDocumentForm
    
    return render(request,'core/add-travel-document.html', context)

@login_required(login_url='/')
def TravelDocumentRead(request):
    context={}
    users=request.user
    
    travel_document_history=TravelDocument.objects.filter(user=users).values()
    print(travel_document_history)
        
    context['travel_document_history'] = travel_document_history
    return render(request, 'core/travel-document.html', context)

@login_required(login_url='/')
def TravelDocumentDelete(request, id):
    travel_history = TravelDocument.objects.get(pk=id)
    if travel_history.delete():
        messages.success(request, 'Documents are SuccessFully Deleted....')
        return redirect('core:travel-document')
    else:
        messages.error(request, "Something wen't to delete Package" )
    
    return render(request, 'core/travel-document.html', {'travel_history': travel_history})

@login_required(login_url='/')
def TravelTicketUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        travel_ticket = TravelDocument.objects.get(pk=id)
        tt_form = TravelTicketUpdateForm(request.POST, request.FILES, instance=travel_ticket)
        if tt_form.is_valid():
            print("Done...")
            tt_form.save()
            messages.success(request, "Ticket Documents are SuccuessFully Updated....")
            return redirect('core:travel-document')
        context['tt_form'] = tt_form
        context['travel_ticket'] = travel_ticket
    else:
        travel_ticket = TravelDocument.objects.get(pk=id)
        
        tt_form = TravelTicketUpdateForm(instance=travel_ticket)
        
        context['tt_form'] = tt_form
        context['travel_ticket'] = travel_ticket
    
    return render(request, 'core/travel-ticket-update.html', context)

@login_required(login_url='/')
def TravelReservationUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        travel_reservation = TravelDocument.objects.get(pk=id)
        tr_form = TravelReservationUpdateForm(request.POST, request.FILES, instance=travel_reservation)
        if tr_form.is_valid():
            print("Done...")
            tr_form.save()
            messages.success(request, "Reservaion Documents are SuccuessFully Updated....")
            return redirect('core:travel-document')
        context['tr_form'] = tr_form
        context['travel_reservation'] = travel_reservation
    else:
        travel_reservation = TravelDocument.objects.get(pk=id)
        
        tr_form = TravelReservationUpdateForm(instance=travel_reservation)
        
        context['tr_form'] = tr_form
        context['travel_reservation'] = travel_reservation
    
    return render(request, 'core/travel-reservation-update.html', context)

@login_required(login_url='/')
def AddBucketView(request,id):
    context = {}
    destination_id=Destinations.objects.get(pk=id)
    user=request.user
    if request.method == 'POST':
        bucket_form=AddBucketForm(request.POST)
        print(bucket_form)
        if bucket_form.is_valid():
            bucket=bucket_form.save(commit=False)
            bucket.user_id=user.id
            bucket.destination_id=destination_id
            bucket.save()
            messages.success(request, "Your Destination Is Successfully Added In Bucket....")
            print('Done.........')
            return redirect('core:bucket')
    context['bucket_form'] = AddBucketForm
    context['dest'] = destination_id
    return render(request, 'core/add-bucket.html',context)

@login_required(login_url='/')
def BucketView(request):
    context = {}
    
    user=request.user
    bucket_history=Bucket.objects.filter(user=user)
    
    loyalty_history=Loyalty.objects.filter(user=user).values()
     
    context['bucket_history'] = bucket_history
    context['loyalty_history'] = loyalty_history
    return render(request, 'core/bucket.html',context)

@login_required(login_url='/')
def BucketDetails(request, id):
    context = {}
    if request.method == "GET":
        
        bucket_details = Bucket.objects.get(pk=id)
        bucket_itinerary_data = bucket_details.destination_id.details.all()
        print(bucket_itinerary_data)
        print(bucket_details)
        
        context['bucket_details'] = bucket_details
        context['bucket_itinerary_data'] = bucket_itinerary_data
    
        return render(request, 'core/bucket-details.html', context)
    else:
        return HttpResponse("Page not supported")

@login_required(login_url='/')
def BucketDelete(request, id):
    bucket_data_history = Bucket.objects.get(pk=id)
    if bucket_data_history.delete():
        messages.success(request, 'Destination Is SuccessFully Remove....')
        return redirect('core:bucket')
    else:
        messages.error(request, "Something wen't to delete Package" )
    
    return render(request, 'core/bucket.html', {'bucket_data_history': bucket_data_history})

@login_required(login_url='/')
def BucketUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        bucket_data = Bucket.objects.get(pk=id)
        bd_form = AddBucketForm(request.POST, instance=bucket_data)
        if bd_form.is_valid():
            print("Done...")
            bd_form.save()
            messages.success(request, "Bucket Is SuccuessFully Updated....")
            return redirect('core:bucket')
        context['tt_form'] = bd_form
        context['bucket_data'] = bucket_data
    else:
        bucket_data = Bucket.objects.get(pk=id)
        bd_form = AddBucketForm(instance=bucket_data)
        
        context['bd_form'] = bd_form
        context['bucket_data'] = bucket_data
    
    return render(request, 'core/bucket-update.html', context)

@login_required(login_url='/')
def LoyaltyView(request):
    context = {}
    if request.method=='POST':
        
        loyalty_form = LoyaltForm(request.POST)
        
        if loyalty_form.is_valid():
            
            try: 
                cd = loyalty_form.cleaned_data    
            
                pc = Loyalty(
                   
                    loyalty_value = cd['loyalty_value'],
                    user = cd['user'],
                )
                pc.save()

                messages.success(request, "Loyalty Point Is Added successfully......")
                print('Done.........')
                return redirect('core:loyalty')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")
        else:
            print(loyalty_form.errors)

    context['loyalty_form'] = LoyaltForm
    return render(request, 'core/add-loyalty.html',context)

@login_required(login_url='/')
def LoyaltyRead(request):
    context = {}
    
    if 'q' in request.GET:
        q = request.GET['q']
        loyalty = Loyalty.objects.filter(user__icontains=q)
        print(loyalty)
    else:
        loyalty = Loyalty.objects.all().order_by("-created_at")
        print(loyalty)

    context['loyalty'] = loyalty
    
    return render(request, 'core/loyalty.html', context)

@login_required(login_url='/')
def LoyaltyDelete(request, id):
    loyalty_data = Loyalty.objects.get(pk=id)
    if loyalty_data.delete():
        messages.success(request, 'Loyalty Points Is SuccessFully Deleted....')
        return redirect('core:loyalty')
    else:
        messages.error(request, "Something wen't to delete Package" )
    
    return render(request, 'core/bucket.html', {'loyalty_data': loyalty_data})

@login_required(login_url='/')
def LoyaltyUpdate(request, id):
    
    context = {}
    
    if request.method == 'POST':
        loyalty_value = Loyalty.objects.get(pk=id)
        lp_form = LoyaltForm(request.POST, instance=loyalty_value)
        if lp_form.is_valid():
            print("Done...")
            lp_form.save()
            messages.success(request, "Loyalty Points are SuccuessFully Updated....")
            return redirect('core:loyalty')
        context['lp_form'] = lp_form
        context['loyalty_value'] = loyalty_value
    else:
        loyalty_value = Loyalty.objects.get(pk=id)
        lp_form = LoyaltForm(instance=loyalty_value)
        
        context['lp_form'] = lp_form
        context['loyalty_value'] = loyalty_value
    
    return render(request, 'core/loyalty-update.html', context)