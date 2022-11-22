from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from artists.models import *
from django.core.exceptions import ValidationError
from django.db.models import Q

def retrieve(request):
    albums = []
    for album in Album.objects.all():
        albums.append(album)  
    
    return render(request,"albums/retrieve.html", {'albums': albums})

def create(request):
    return render(request, "albums/create.html",{'artists' : Artist.objects.all()})

def store(request):
    album = Album()
    album.name = request.POST['album_name']
    album.cost = request.POST['album_cost']
    album.artist = Artist.objects.get(id = int(request.POST['artist']))
    album.releaseDateTime = request.POST['album_releaseDateTime']
    album.is_approved = request.POST.get('album_is_approved', False)
    if album.is_approved == 'on':
        album.is_approved = True

    album.save()
    return retrieve(request)
    