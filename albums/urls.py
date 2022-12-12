from django.urls import path
from albums import views
urlpatterns = [
    path('', views.AlbumView.as_view()),
    path('create/', views.CreateAlbumView.as_view()),
    path('store/',views.StoreAlbumView.as_view(),name="albums/store")
]
