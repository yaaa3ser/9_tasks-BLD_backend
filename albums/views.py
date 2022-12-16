from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from artists.models import *
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.views import View

from django.db.models.signals import pre_save
from django.dispatch import receiver

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import *
from rest_framework import status, generics

class AlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, **kwargs):
    if instance.name =='':
        album = instance.album
        instance.name = album.name
    
class RetrieveAlbumView(View):
    def get (self, request):
        return render(request,"albums/retrieve.html", {'albums': Album.objects.all()})
    
class CreateAlbumView(View):
    def get(self, request):
        return render(request, "albums/create.html",{'artists' : Artist.objects.all()})

class StoreAlbumView(View):
    def post(self, request):
        album = Album()
        album.name = request.POST['album_name']
        album.cost = request.POST['album_cost']
        album.artist = Artist.objects.get(id = int(request.POST['artist']))
        album.releaseDateTime = request.POST['album_releaseDateTime']
        album.is_approved = request.POST.get('album_is_approved', False)
        if album.is_approved == 'on':
            album.is_approved = True

        album.save()
        return RetrieveAlbumView.get(self,request)
        