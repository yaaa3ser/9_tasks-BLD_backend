## **_*Permissions and Django Filters*_**
----------------------------------------

- Added a relationship field to the Artist model that maps an artist to a user instance.

```py
from django.db import models 
from users.models import User

class Artist(models.Model):
    stageName = models.CharField(max_length=100, unique=True ,verbose_name = 'Name')
    socialLink = models.URLField(max_length=250, verbose_name = 'social media')      
--> user = models.OneToOneField(User,on_delete=models.CASCADE) <--
```

- GET should return a list of approved albums

  - responnse
    ```json
    [
        {
            "id": 1,
            "artist": {
                "id": 1,
                "stageName": "yasser issa",
                "socialLink": "https://www.twitter.com/yasser"
            },
            "name": "mesh 55555",
            "releaseDateTime": "2022-12-18T05:44:42+03:00",
            "cost": "1200.00",
            "is_approved": true
        },
        {
            "id": 2,
            "artist": {
                "id": 1,
                "stageName": "yasser issa",
                "socialLink": "https://www.twitter.com/yasser"
            },
            "name": "55555",
            "releaseDateTime": "2022-12-18T07:40:43+03:00",
            "cost": "1300.00",
            "is_approved": false
        }
    ]
    ```
    - Permit any type of request whether it's authenticated or not

    - It doesn't make sense to return all albums that we have to the frontend at once, if we have hundreds of thousands of albums, the user's screen will not be able to render that much data, instead we should support pagination.
    

    ***settings.py***

    ```python
    REST_FRAMEWORK = {
        ...

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 2,

        ...
        }
    ```
    - [see serializers](albums/serializers.py)

    - [see views](albums/views.py)

- Bonus: Can you create and use custom queryset manager that only returns approved albums?

***albums.models.py***
```python
class AlbumQuery (models.QuerySet):
    def is_approved(self):
        return self.filter(isApproved=True)

    def search(self, q):
        return self.filter(name__icontains=q)
```


- POST should accept a JSON body, create an album, and raise proper validation errors for all fields

    - The request body should look like: { "name": ..., "release_datetime": ..., "cost": ..., }
    - Permit only authenticated requests
    - The request must be authenticated by a user who is also an artist
    - The created album will be mapped to the artist who made the request
    - 403 Forbidden error should be raised if a POST request is not authenticated or if it's authenticated by a
    user who isn't an artist

    - [see edited views](albums/views.py)
- Using django-filter , support the following optional filters for GET requests:
    - Cost greater than or equal
    - Cost less than or equal
    - Case-insensitive containment


***albums.filters.py***
```py
import django_filters
from albums.models import *


class AlbumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cost__lte = django_filters.NumberFilter(field_name="cost", lookup_expr='lte')
    cost__gte = django_filters.NumberFilter(field_name="cost", lookup_expr='gte')

    class Meta:
        model = Album
        fields = ['name', 'cost__lte', 'cost__gte']

```

***albums.views.py***
 ```py
class ListAlbum(generics.ListAPIView):
    ...    
    filterset_class = AlbumFilter
    ...
 ```