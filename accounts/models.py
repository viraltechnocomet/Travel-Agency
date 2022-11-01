from asyncio.windows_events import NULL
from email.policy import default
from enum import unique
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,AbstractUser,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

USER_TYPES=[
    ('ADMIN', 'admin'),
    ('MANAGER', 'manager'),
    ('AGENT', 'agent'),
    ('CLIENT', 'client'),
]
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,null=True,blank=True)
    type = models.CharField(max_length=10,choices=USER_TYPES,null=True,blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    # profile_pic=models.ImageField(max_length=225, upload_to='profile_pic', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return_str = None
        if self.username:
            return_str = self.username
        else:
            return_str = self.email
        return return_str

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True


    