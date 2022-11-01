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

from core.forms import CreateUserCustomForm, AddManagerForm
from accounts.models import CustomUser
from django.conf import settings
from core.forms import AddManagerForm,AddAgentForm
import os

from django.core import files
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

from templates import *
from django.contrib import messages
from accounts.models import USER_TYPES

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"

class DashboardView(View):
    template_name = './core/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {"demo":"value"}
        return render(request, self.template_name,context=context)

    def post(self, request, *args, **kwargs):
        ...
        
# def AddManager(request):
#     context={}
#     context['form'] = AddManagerForm
#     return render(request,'core/add-manager.html',context)

def AddAgent(request):
    context={}
    context['form'] = AddAgentForm
    return render(request,'core/add-agent.html',context)



class AddManagerView(View):

    def get(self,request):
        form = AddManagerForm(request.POST or None)
        return render(request, "core/add-manager.html", {"form": form })

    def post(self, request):
        msg     = None
        success = False

        if request.method == "POST":
            print(request.POST)
            form = AddManagerForm(request.POST)
            print(form.errors)
            # print(form)
            if form.is_valid():
                # print("It's okkkkkkk......")
                form.save()
                # group = Group.objects.get(name='client')
                fname=form.cleaned_data.get("first_name")
                lname=form.cleaned_data.get("last_name")
                uname = form.cleaned_data.get("username")
                em = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password")
                # user = authenticate(username=uname, password=raw_password)
                # user.groups.add(group)

                msg     = messages.add_message(request, messages.SUCCESS,'User created Successfully!')
                success = True
                
                return redirect("/core/add-manager/")

            else:
                msg = ('Form is not valid',)
                form.add_error(None,'Form is not valid')
        else:
            form = AddManagerForm()

        return render(request, "core/add-manager.html", {"form": form, "msg" : msg, "success" : success })

# class AddManagerView(View):            
#     if request.method == 'POST':
#         form = AddManagerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             fname = form.cleaned_data.get('first_name')
#             lname = form.cleaned_data.get('last_name')
#             uname = form.cleaned_data.get('username')
#             em = form.cleaned_data.get('email')
#             pw = form.cleaned_data.get('password')
#             user = authenticate(username=uname, password=pw)
#             login(request, user)
#             return redirect('/core/add-manager/')
#     else:
#         form = AddManagerForm()
#     return render(request, 'add-manager.html', {'form': form})

# class AddManagerView(View): 
#     def addmanager(request):   
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 fname = form.cleaned_data.get('first_name')
#                 lname = form.cleaned_data.get('last_name')
#                 uname = form.cleaned_data.get('username')
#                 em = form.cleaned_data.get('email')
#                 pw = form.cleaned_data.get('password')
#                 user = authenticate(username=uname, password=pw)
#                 login(request, user)
#                 return HttpResponse("User created successfully!")
#                 return render(request, 'core/add-manager.html', {'form': form})
#         else:
#             form = AddManagerForm()()
#             return render(request, 'core/add-manager.html', {'form': form})



    # {% csrf_token %}
    # {{ form }}
