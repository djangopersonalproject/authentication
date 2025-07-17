from django.contrib import admin
from django.urls import path
from .views import Home_view,Register_view,UserLogin_view,UserLogout
urlpatterns = [
    path("",Home_view.as_view(),name="home"),
    path('register/',Register_view.as_view(),name='register'),
    path('user-login/',UserLogin_view.as_view(),name='login'),
    path('logout/',UserLogout.as_view(),name='logout'),
]
