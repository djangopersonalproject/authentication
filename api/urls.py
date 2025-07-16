from django.contrib import admin
from django.urls import path
from .views import Home_view,Register_view
urlpatterns = [
    path("",Home_view.as_view(),name="home"),
    path('register/',Register_view.as_view(),name='register'),
]
