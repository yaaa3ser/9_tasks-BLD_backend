import pytest
from ..models import Artist
from artists.serializers import ArtistSerializer
from rest_framework.views import status
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db
class TestArtists:
    def test_creation_with_wrong_data(self):
        artist = ArtistSerializer(data={})
        assert artist.is_valid() == False

    def test_creation_with_correct_data(self):
        artist = Artist()
        artist.stageName = "yasser"
        artist.socialLink = "www.facebook.com/yasser"
        artist.save()
        assert len(Artist.objects.all()) == 1
        