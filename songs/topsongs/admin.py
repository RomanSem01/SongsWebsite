from django.contrib import admin
from .models import Band, Genre, Song, Playlist, Subscription


class PlaylistAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated', ]


admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Subscription)
