from django.db import models

# Create your models here.


class Artist(models.Model):
    stageName = models.CharField(max_length=50, unique=True)
    socialLink = models.URLField()

    class Meta:
        ordering = ['stageName']

    def __str__(self):
        return self.stageName
