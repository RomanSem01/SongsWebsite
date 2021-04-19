"""songs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from topsongs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('song/<int:song_id>', views.search_song, name='search_song'),
    path('band/<int:band_id>', views.band_info, name='band_info'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('remove_playlist/<int:playlist_id>', views.remove_playlist, name='remove_playlist'),
    path('search_playlists/', views.search_playlists, name='search_playlists'),
    path('add_to_playlist/<int:song_id>',
         views.add_to_playlist, name='add_to_playlist'),
    path('playlists/', views.display_playlists, name='display_playlists'),
    path('playlist/<int:playlist_id>', views.playlist_info, name='playlist_info'),
    path('remove_from_playlist/<int:playlist_id>/<int:song_id>',
         views.delete_from_playlist, name='delete_from_playlist'),
    path('my_subscriptions/', views.show_subscriptions, name='show_subscriptions'),
    path('subcribe/<int:playlist_id>', views.subscribe, name='subscribe'),

    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('show_user/<int:user_id>', views.show_user, name='show_user'),
]
