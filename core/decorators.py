from .models import UserSettings
from django.shortcuts import (
    redirect,
)

def is_admin(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.type == "ADMIN" or request.user.is_superuser:
            return view_func(request, *args, **kwargs)    
        else:
            return redirect("/")
    return wrap

def is_manager(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.type == "MANAGER" or request.user.is_superuser:
            return view_func(request, *args, **kwargs)    
        else:
            return redirect("/")
            
    return wrap

def is_agent(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.type == "AGENT" or request.user.is_superuser:
            return view_func(request, *args, **kwargs)    
        else:
            return redirect("/")
            
    return wrap