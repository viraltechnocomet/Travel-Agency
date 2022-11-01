from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
# from accounts import models

User = get_user_model()

class addmanager(models.Model):
    pass

class addagent(models.Model):
    pass

class addclient(models.Model):
    pass