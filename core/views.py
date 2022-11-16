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
        context={
            'form': form
        }
        return render(request, "core/add-user.html", context)

    def post(self,request):
        form = SignUpForm(data = request.POST)
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
    


def ItineraryView( request):
    
    context = {}
    courntryForm = CourntryForm(request.POST)
    categoryForm = CategoryForm(request.POST)
    activityForm = ActivityForm(request.POST)
    imageForm = ImageForm(request.POST)
    itineraryForm = ItineraryForm(request.POST)
    packageForm = PackageForm(request.POST)
    selected_PackageForm = Selected_PackageForm(request.POST)

    if request.method=='POST':
        if courntryForm.is_valid():
            courntryForm.save()
        if categoryForm.is_valid():
            categoryForm.save()
        if activityForm.is_valid():
            activityForm.save()
        if imageForm.is_valid():
            imageForm.save()
        if itineraryForm.is_valid():
            itineraryForm.save()
        if packageForm.is_valid():
            packageForm.save()
        if selected_PackageForm.is_valid():
            selected_PackageForm.save()

    context['courntryForm'] = CourntryForm
    context['categoryForm'] = CategoryForm
    context['activityForm'] = ActivityForm
    context['imageForm'] = ImageForm
    context['itineraryForm'] = ItineraryForm
    context['packageForm'] = PackageForm
    context['selected_PackageForm'] = Selected_PackageForm

    return render(request,'core/add-itinerary.html', context)
