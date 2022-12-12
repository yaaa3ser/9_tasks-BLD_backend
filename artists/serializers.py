from rest_framework import serializers
from rest_framework.validators import ValidationError,UniqueValidator
from .models import *
from albums.serializers import *

def checkBlank(name):
    if name == '':
        raise ValidationError('You must enter a Stage Name')
    
    
class ArtistSerializer(serializers.ModelSerializer):
    stageName = serializers.CharField(
        validators=[checkBlank ,UniqueValidator(queryset=Artist.objects.all())]
    )
    socialLink = serializers.URLField(validators=[checkBlank])
    albums = AlbumSerializer(many = True)
    
    class Meta:
        model = Artist
        fields = '__all__'
        
