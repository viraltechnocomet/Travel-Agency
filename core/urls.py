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
    
    
]
