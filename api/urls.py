from django.contrib import admin
from django.urls import path
from .views import (Register_view,UserLogin_view,UserLogout,
NoteDelete_view,NoteCreateView,NoteDetail_view,Notelist_view,NoteUpdate_view)
urlpatterns = [
    path('register/',Register_view.as_view(),name='register'),
    path('user-login/',UserLogin_view.as_view(),name='login'),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('note/',NoteCreateView.as_view(),name="note"),
    path('note-list/',Notelist_view.as_view(),name='note_list'),
    path('note-update/<int:pk>/',NoteUpdate_view.as_view(),name='note-update'),
    path('note-detail/<int:pk>/',NoteDetail_view.as_view(),name="note-detail"),
    path('note-delete/<int:pk>/',NoteDelete_view.as_view(),name='note-delete'),
]
