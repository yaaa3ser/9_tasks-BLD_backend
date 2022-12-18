from rest_framework import generics
import django_filters
from albums.models import Album


class AlbumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cost__lte = django_filters.NumberFilter(field_name="cost", lookup_expr='lte')
    cost__gte = django_filters.NumberFilter(field_name="cost", lookup_expr='gte')

    class Meta:
        model = Album
        fields = ['name', 'cost__lte', 'cost__gte']