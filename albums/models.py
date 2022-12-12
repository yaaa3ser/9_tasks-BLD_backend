from django.db import models
from django.utils import timezone
from artists.models import Artist
from django.db.models.functions import Coalesce
from model_utils.models import StatusModel


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

class Album(TimeStampedModel):
    name = models.CharField(max_length=30, default='New Album')
    releaseDateTime = models.DateTimeField(default=timezone.now, blank=False)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='albums')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=100,blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return self.name
    
