from rest_framework import serializers
from rest_framework.validators import ValidationError,UniqueValidator
from .models import *
from albums.serializers import *
from albums.models import Album
from users.serializers import UserSerializer
def checkBlank(name):
    if name == '':
        raise ValidationError('You must enter a Stage Name')
    
class AlbumSerializerForArtist(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
  
class ArtistSerializer(serializers.ModelSerializer):
    stageName = serializers.CharField(
        validators=[checkBlank ,UniqueValidator(queryset=Artist.objects.all())]
    )
    socialLink = serializers.URLField(validators=[checkBlank])
    albums = AlbumSerializerForArtist(many = True)
    user = UserSerializer
    
    class Meta:
        model = Artist
        fields = '__all__'
        
class CreateArtistSerializer(serializers.ModelSerializer):
    stageName = serializers.CharField(
        validators=[checkBlank ,UniqueValidator(queryset=Artist.objects.all())]
    )
    socialLink = serializers.URLField(validators=[checkBlank])
    user = UserSerializer
    
    class Meta:
        model = Artist
        fields = '__all__'
