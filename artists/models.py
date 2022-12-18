from django.db import models
from users.models import User
# Create your models here.


class Artist(models.Model):
    stageName = models.CharField(max_length=50, unique=True)
    socialLink = models.URLField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['stageName']

    def __str__(self):
        return self.stageName
