from django.contrib import admin
from .models import *
from albums.models import *
# Register your models here.
class AlbumAdmin(admin.TabularInline):
    model = Album

class ArtistAlbum(admin.ModelAdmin):
    def Approved_Albums(self,obj):
        return len(obj.albums.filter(is_approved=True))
    
    list_display = ('stageName', 'socialLink', 'Approved_Albums')
    
    inlines = [AlbumAdmin]

admin.site.register(Artist,ArtistAlbum)

