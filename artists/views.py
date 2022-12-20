from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from albums.models import *
from django.core.exceptions import ValidationError
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated , AllowAny

class ArtistView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
class ArtistCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArtistSerializer
    
    def post(self, request):
        data = request.data
        user = request.user
            
        try:
            if user.artist:
                return Response("This user is already an artist" , status=status.HTTP_403_FORBIDDEN)
        except:
            data['user'] = user.id
            serializer = CreateArtistSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveArtistView(View):
    def get (self, request):
        artistsWithAlbums = []
        for artist in Artist.objects.all():
            artistsWithAlbums.append({'artist':artist,'albums':artist.albums.all()})
        
        return render(request,"artists/retrieve.html",{'artistsWithAlbums' : artistsWithAlbums})
    
class CreateArtistView(View):
    
    def get(self,request, errors={}):
        return render(request, "artists/create.html",{"errs":errors})
    
class StoreArtistView(View):
    def post(self, request):
        artist = Artist()
        artist.stageName = request.POST['sn']
        artist.socialLink = request.POST['sl']
        try :
            artist.full_clean()
            artist.save()
            return RetrieveArtistView.get(self, request)
        except ValidationError as validations:
            errors = validations
            return render(request, "artists/create.html",{"errs":errors})

