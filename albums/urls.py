from django.urls import path
from albums import views
urlpatterns = [
    path('', views.retrieve),
    path('create/', views.create),
    path('store/',views.store,name="albums/store")
]
