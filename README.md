## **_*Project basics, models, and queries | Django Admin and Managers | Forms, Templates, and Views*_**

<br/>

  **For this task and the following ones, we'll try to build a music platform on which artists can sign up and put up their albums for sale**

  - Created a Django project called musicplatform
  - Created an app artists
  - In artists Created an Artist model with some fields
  - Created an app albums
  - In albums Created an Album model with some fields
  - used ```manage.py shell``` to test some queries such that: (Task1 & 2)


      **_create some artists_**
      ```python
      artist = Artist(stageName='hosam issa',socialLink='https://www.twitter.com/hosamissa')
      artist.save()
      Artist.objects.create(stageName='yasser issa',socialLink='https://www.facebook.com/yasserissa')
      artist.save()
      artist = Artist(stageName='ahmed issa',socialLink='https://www.instagram.com/ahmedissa')
      artist.save()
      ```

      **_list down all artists_**
      ```python
      artists = Artist.objects.all()
      print(artists)
      ```

      **_list down all artists sorted by name_**
      ```python
      print(Artist.objects.order_by('stageName'))
      ```

      **_list down all artists whose name starts with a_**
      ```python
      artists = Artist.objects.filter(stageName__startswith='a')
      print(artists)
      ```

      **_create some albums and assign them to any artists_**
      ```python
      artist1 = Artist.objects.get(pk=1)
      album1 = Album(name = 'bya3' , artist = artist1 , cost = 50.00 )
      artist2 = Artist.objects.get(pk=2)
      album2 = Album.objects.create(name = '5555' , artist = artist2 , cost = 200.00 )
      ```

      **_get the latest released album_**
      ```python
      albums = list(Album.objects.order_by('releaseDateTime').values())
      print(albums[len(albums)-1])
      ```

      **_get all albums released before today_**
      ```python
      Album.objects.filter(releaseDateTime__lt=datetime.now())
      ```

      **_get all albums released today or before but not after today_**
      ```python
      Album.objects.filter(releaseDateTime__lte=datetime.now())
      ```

      **_count the total number of albums_**
      ```python
      albums = Album.objects.all()
      print(len(albums))
      ```

      **_```but it is not the best, so the optimized is :```_**

      ```python
      Album.objects.count()
      ```

      so you should always use count() rather than loading all of the record into Python objects and calling len() on the result (unless you need to load the objects into memory anyway, in which case len() will be faster).
      <br/>
      **_for each artist, list down all of his/her albums_**
      ```python
      artists = Artist.objects.all()
      for artist in artists:
          print(artist, artist.albums.all())
      ```

      **_list down all albums ordered by cost then by name (cost has the higher priority)_**
      ```python
      Album.objects.order_by('-cost' , 'name')
      ```

      **_The admin shouldn't be able to modify the creation time field on the album_**
      ```python
      class AlbumAdmin(admin.ModelAdmin):
          readonly_fields = ('creationDateTime',)
      ```

      **_Add a help text that would show up under the previously mentioned boolean field on the django admin form_**
      <br/>

      **_from admin form not the field itself_**
      ```python
      class AlbumAdmin(admin.ModelAdmin):
          readonly_fields = ('creationDateTime',)

          def get_form(self, request, obj=None, change=False, **kwargs):
              form = super().get_form(request, obj=obj, change=change, **kwargs)
              form.base_fields["is_approved"].help_text = "Approve the album if its name is not explicit"
              return form

      admin.site.register(Album,AlbumAdmin)
      ```

      **_ When viewing the list of artists, there must be a column to show the number of approved albums for each artist _**
      ```python
      class ArtistAlbum(admin.ModelAdmin):
          def Approved_Albums(self,obj):
              return len(obj.albums.filter(is_approved=True))

          list_display = ('stageName', 'socialLink', 'Approved_Albums')
      ```

      **_Modify the artist queryset so that I can order the list of artists by the number of their approved albums_**
      ```python
      Artist.objects.filter(albums__is_approved = True).alias(approved_albums = Count('albums')).order_by('approved_albums')
      ```

      **_ Allow the admin to create albums for the artist from from the artist's editing form_**
      ```python
      class AlbumAdmin(admin.TabularInline):
          model = Album

      class ArtistAlbum(admin.ModelAdmin):
          inlines = [AlbumAdmin]

      admin.site.register(Artist,ArtistAlbum)
      ```
      </br>
## **_*Task3 ==>Forms, Templates, and Views*_**

  - Instead of having an explicit created_at field in the Album model, inherit from TimeStampedModel
    ```python
    class TimeStampedModel(models.Model):
        created_on = models.DateTimeField(auto_now_add=True)
        
        class Meta:
            abstract = True

    class Album(TimeStampedModel):
      ...
    ```
  
  - Created a form that allows a user to create an artist (it should be available at http://localhost:8000/artists/create)
    - [edit views](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/artists/views.py)
    - [edit urls](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/artists/urls.py)
    - [add templates](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/templates/artists/create.html)

  - Created a form that allows a user to create an album (it should be available at https://localhost:8000/albums/create)
    - [edit views](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/albums/views.py)
    - [edit urls](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/albums/urls.py)
    - [add templates](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/templates/albums/create.html)

  - Create a template view that lists all the albums grouped by each artist (it should be available at https://localhost:8000/artists/)
    - [edit views](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/artists/views.py)
    - [edit urls](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/artists/urls.py)
    - [add templates](https://github.com/yaaa3ser/9_tasks-BLD_backend/blob/first_3tasks/templates/artists/create.html)
  


