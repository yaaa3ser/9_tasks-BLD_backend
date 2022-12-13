from django.contrib import admin
from .models import User
from .forms import UserForm
from django.contrib.auth.admin import UserAdmin

class User_Admin(UserAdmin):
    form = UserForm
    
admin.site.register(User,User_Admin)