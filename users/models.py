from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # override email to be add unique = true
    email = models.CharField(max_length=256, unique=True)
    
    bio = models.CharField(max_length=256, blank=True)