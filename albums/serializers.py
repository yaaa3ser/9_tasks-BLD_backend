from rest_framework import serializers
from rest_framework.validators import ValidationError,UniqueValidator
from .models import *
from artists.serializers import *

class ArtistSerializerForAlbums(serializers.ModelSerializer):
    stageName = serializers.CharField()
    socialLink = serializers.URLField()    
    class Meta:
        model = Artist
        exclude= ['user']


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializerForAlbums()
    class Meta:
        model = Album
        exclude= ['created_on']
        
class CreateAlbumSerializer (serializers.ModelSerializer):
    # songs = SongSerializer(many=True, required=False)

    class Meta:
        model = Album
        exclude = ('is_approved',)