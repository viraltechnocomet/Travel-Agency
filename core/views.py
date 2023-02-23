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
    if request.method=='POST':
        itineraries = request.POST.getlist("details")

        obj_itineraries = list(Itinerary.objects.filter(pk__in = itineraries))
        
        package = ItineraryPackageForms(request.POST,request.FILES)
        
        if package.is_valid():
            package.save()
            
            try: 
                cd = package.cleaned_data
            
                pc = Destinations(
                    
                    image = request.FILES['image'],
                    name = cd['name'],
                    # from_date = cd['from_date'],
                    # to_date = cd['to_date'],
                    # days = cd['days'],
                    # nights = cd['nights'],
                    # price = cd['price'],
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
            
            # if Package.package_image!=None and Package.package_image!='':
            #     package_datas.package_image=Package.package_image
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
def AddCart(request,id):
    
    context = {}
    
    if request.method == "POST":
        itinerary_cart = request.POST.getlist("itinerary_cart[]")
        # print(itinerary_cart)
        # obj_cart= AddCartPackage.objects.get(pk__in=itinerary_cart)
        # print(obj_cart)
        # iti_cart_value=""
        # for i in itinerary_cart:
        #     iti_cart_value=i+','+iti_cart_value
        #     print(iti_cart_value)
        # obj_cart.itinerary_cart=iti_cart_value
        # obj_cart.save()
        obj_itineraris = Itinerary.objects.filter(pk__in=itinerary_cart)
        print(obj_itineraris)

        package_cart_data = Destinations.objects.get(pk=id)
        package_itinerary_details= package_cart_data.details.all().values('id','destination')
        cart_form = AddCartForm(request.POST)
        print(request.POST)

        if cart_form.is_valid():
            # cart_form.save()
            
            try: 
                cd = cart_form.cleaned_data
                pc = AddCartPackage(
                    
                    start_date = cd['start_date'],
                    end_date = cd['end_date'],
                    adults = cd['adults'],
                    children = cd['children'],
                    infant = cd['infant'],
                )
                
                pc.save()
                for obj in obj_itineraris:
                    pc.itinerary_cart.add(obj)
                pc.save()
                # pc.itinerary_cart.save(iti_cart_value)
                
                messages.success(request, "Package Successfully Added In Cart")
                print('Done.........')
            except ValueError:
                messages.error(request, "OPPS.... SORRY YOUR DATA ARE NOT SAVE......")
                print("Oppsssssss")

            return redirect('core:package')
        
        context['cart_forms'] = cart_form
        context['package_cart_data'] = package_cart_data
        context['package_itinerary_details'] = package_itinerary_details
        
    else:
        package_cart_data = Destinations.objects.get(pk=id)
        package_itinerary_details= package_cart_data.details.all().values('id','destination')
        cart_form = AddCartForm()
        context['cart_forms'] = cart_form
        context['package_cart_data'] = package_cart_data
        context['package_itinerary_details'] = package_itinerary_details
    
    return render(request, 'core/add-cart.html',context)


def CartDetails(request):
    context = {}
    # c_user= request.user.id
    # print(c_user)
    # c_data=CustomUser.objects.filter(pk=c_user)
    # print(c_data)
    # cart_detail=
    # cart_data=AddCartPackage.objects.get(id=38)
    # print(cart_data)
    # context['cart_data'] = cart_data
            
    return render(request, 'core/cart.html',context)

def RatePackage(request,id):
    context = {}
    destination_id=Destinations.objects.get(pk=id)
    user=request.user
    if request.method == 'POST':
        rate_form=RateForm(request.POST)
        print(rate_form)
        if rate_form.is_valid():
            rate=rate_form.save(commit=False)
            rate.user_id=user.id
            rate.destination_id=destination_id
            rate.save()
            messages.success(request, "Rating Are Successfully Given To " + destination_id.name)
            print('Done.........')
            return redirect('core:package')
    context['rate_form'] = RateForm
    context['des'] = destination_id
    return render(request, 'core/rate-package.html',context)

@login_required(login_url='/')
def AccommodationView(request):
    
    context = {}
    if request.method=='POST':
        
        accommodation = AccommodationForm(request.POST,request.FILES)
        
        if accommodation.is_valid():
            # accommodation.save()
            try: 
                cd = accommodation.cleaned_data
            
                pc = Accomodation(
                   
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
    acc = Accomodation.objects.all().values_list('id')
    if 'q' in request.GET:
        q = request.GET['q']
        acc = Accomodation.objects.filter(ac_name__icontains=q)
    else:
        acc = Accomodation.objects.all().order_by("id")

    context['acc'] = acc
    return render(request, 'core/accommodation.html', context)

@login_required(login_url='/')
def AccommodationDelete(request, id):
    accomodation_data = Accomodation.objects.get(id=id)
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
        accommodation_datas = Accomodation.objects.get(pk=id)
        ac_form = AccommodationUpdateForm(request.POST, request.FILES, instance=accommodation_datas)
        if ac_form.is_valid():
            print("Done...")
            ac_form.save()
            messages.success(request, "Accommodation is SuccuessFully Updated....")
            return redirect('core:accommodation')
        context['ac_form'] = ac_form
        context['accommodation_datas'] = accommodation_datas
    else:
        accommodation_datas = Accomodation.objects.get(pk=id)
        
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