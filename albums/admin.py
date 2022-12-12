from django.contrib import admin
from .models import *
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["is_approved"].help_text = "Approve the album if its name is not explicit"
        return form


admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)