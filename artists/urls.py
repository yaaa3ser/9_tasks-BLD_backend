from django.urls import path
from artists import views
urlpatterns = [
    path('', views.retrieve),
    path('create/', views.create),
    path('store/',views.store,name="artists/store")
]
