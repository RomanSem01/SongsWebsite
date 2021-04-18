from django.contrib import admin
from .models import Band, Genre, Song, Playlist

admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Playlist)