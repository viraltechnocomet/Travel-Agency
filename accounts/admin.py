from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.utils.html import format_html
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CustomUserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email','password1','password2',)

    def clean_password2(self):
        print("in user create form")
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # if not self.is_superuser:
        #     user.group = Group.objects.get(name='admin')
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def clean_password(self):
        print("in clean password")
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # list_display = ('__str__', 'change_button',"status_button", 'delete_button')
    list_display = ('__str__', 'change_button',"status_button", 'delete_button')
    search_fields = ('email',)
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','groups' , 'is_staff', 'is_active', 'is_superuser')}
        ),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('groups','is_staff', 'is_active','is_superuser')}),
    )
    
    search_fields = ('email',)
    ordering = ('email',)

    

    def change_button(self, obj):
        app = obj._meta.app_label
        model = obj._meta.model_name

        return format_html(f"<a href='/admin/{app}/{model}/{obj.id}/' class='editlink'>Edit</a>")

    def status_button(self, obj):
        app = obj._meta.app_label
        model = obj._meta.model_name

        if obj.is_active:
            return format_html(f"Active")
        else:
            return format_html(f"Inactive")

    def delete_button(self, obj):
        app = obj._meta.app_label
        model = obj._meta.model_name

        return format_html(f"<a href='/admin/{app}/{model}/{obj.id}/delete/' class='deletelink'></a>")

    status_button.short_description = 'Status'
    change_button.short_description = 'Edit'
    delete_button.short_description = 'Remove'

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(email=request.user.email)
    
    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)