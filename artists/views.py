from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from albums.models import *
from django.core.exceptions import ValidationError
from django.db.models import Q

def retrieve(request):
    artistsWithAlbums = []
    for artist in Artist.objects.all():
        artistsWithAlbums.append({'artist':artist,'albums':artist.albums.all()})
    
    return render(request,"artists/retrieve.html",{'artistsWithAlbums' : artistsWithAlbums})


def create(request, errors={}):
    return render(request, "artists/create.html",{"errs":errors})

def store(request):
    artist = Artist()
    artist.stageName = request.POST['sn']
    artist.socialLink = request.POST['sl']
    try :
        artist.full_clean()
        artist.save()
        return retrieve(request)
    except ValidationError as validations:
        errors = validations
        return create(request,errors)

