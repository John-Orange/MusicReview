from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songs/',views.songs, name='songs'),
    path('songDetail/<int:id>', views.songDetail, name='songDetail'),
    path('newMusicType/', views.newMusicType, name='newMusicType'),
    path('newAuthor/', views.newAuthor, name='newAuthor'),
    path('newSong/', views.newSong, name='newSong'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]