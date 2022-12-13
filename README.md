## **_*Django Extensions, Knox Token Authentication*_**

<br/>

- Removed the old authentication that created before.
- Created an app users
- In the users app, extended Django's user model by inheriting from AbstractUser to include an optional bio CharField.

  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser

  class User(AbstractUser):
      bio = models.CharField(max_length=256, blank=True)
  ```

- On django admin, this field should be displayed as a TextArea</br>
  `forms.py:`
  ```python
  from django import forms
  from .models import User

      class UserForm(forms.ModelForm):
          bio = forms.CharField(widget = forms.Textarea)
          class Meta:
              model = User
              fields = '__all__'
      ```

      ```admin.py:```

      ```python
      from django.contrib import admin
      from .models import User
      from .forms import UserForm
      from django.contrib.auth.admin import UserAdmin

      class User_Admin(UserAdmin):
          form = UserForm

      admin.site.register(User,User_Admin)
      ```

- Created an app authentication
- In the authentication app, supported a:-

  - POST _authentication/register/_ endpoint that creates users and
  - POST _authentication/login/_ endpoint that returns a KnoxToken and the user's data in a nested object.

    - [edit authentication serializers](authentication/serializers.py)
    - [edit authentication views](authentication/views.py)
    - [edit authentication urls](authentication/urls.py)

- Created a POST authentication/logout/ endpoint that logs the user out from the app by invalidating the knox token

  - [in authentication urls](authentication/urls.py)

- In the users app, created a user detail endpoint /users/< pk > that supports the following requests:

  - GET returns the user data matching the given pk , namely, it should return the user's id , username , email and bio .
  - return 404 status code if the user with the given pk does not exist
  - Support updating the bio , username , and email fields via PUT, PATCH
  - Allow update requests if the user making the request is the user in the < pk > of the url.

    - [edit users serializers](users/serializers.py)
    - [edit users views](users/views.py)
    - [edit users urls](users/urls.py)

- Added TokenAuthentication to the default authentication classes

  [edit settings file](musicplatform/settings.py)

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'knox.auth.TokenAuthentication',
      ]
  }
  ```
