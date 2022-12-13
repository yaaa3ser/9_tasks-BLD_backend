from django.urls import path
from .views import LoginView,RegisterView
from knox import views as knox_views

urlpatterns = [
    path('login/',LoginView.as_view(), name='knox-login'),
    path('register/',RegisterView.as_view(), name='knox-login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]
