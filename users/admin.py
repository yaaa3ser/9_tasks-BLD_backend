from django.contrib import admin
from .models import User
from .forms import UserForm
from django.contrib.auth.admin import UserAdmin


class User_Admin(UserAdmin):
    list_display = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    form = UserForm
    
admin.site.register(User,User_Admin)