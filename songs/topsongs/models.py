from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


class Band(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    year = models.IntegerField()
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100, null=False)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=False)
    description = models.TextField()
    year = models.IntegerField()
    video = EmbedVideoField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    songs = models.ManyToManyField(Song)

    class Meta:
        unique_together = (('name', 'user'))

    def __str__(self):
        return self.name
