from django.urls import path
from artists import views
urlpatterns = [
    path('', views.RetrieveArtistView.as_view()),
    path('api/', views.ArtistView.as_view()),
    path('create/', views.CreateArtistView.as_view()),
    path('store/',views.StoreArtistView.as_view())
]
