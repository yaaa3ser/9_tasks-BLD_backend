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
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .filters import AlbumFilter

# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 3



@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, **kwargs):
    if instance.name =='':
        album = instance.album
        instance.name = album.name
        
class AlbumView(generics.ListAPIView):
    authentication_classes = []
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AlbumFilter
    
    # pagination_class = LargeResultsSetPagination
    
class AlbumCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateAlbumSerializer
    
    def post(self, request):
        data = request.data
        user = request.user
        print(data ['artist'])
        print(Artist.objects.get(user=user).id)
            
        if(data ['artist'] != Artist.objects.get(user=user).id):
            return Response("user is not registered as artist" , status=status.HTTP_403_FORBIDDEN)
        
        serializer = CreateAlbumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class RetrieveAlbumView(View):
#     def get (self, request):
#         return render(request,"albums/retrieve.html", {'albums': Album.objects.all()})
    
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
        