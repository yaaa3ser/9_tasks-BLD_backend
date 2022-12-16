from django.urls import path
from albums import views
urlpatterns = [
    path('', views.RetrieveAlbumView.as_view()),
    path('api/', views.AlbumView.as_view()),
    path('create/', views.CreateAlbumView.as_view()),
    path('store/',views.StoreAlbumView.as_view(),name="albums/store")
]
