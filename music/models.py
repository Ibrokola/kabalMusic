from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Album(models.Model):
    '''The Album model which creates tables in the database for album objects storage'''
    user = models.ForeignKey(User)
    artist = models.CharField(max_length=500)
    album_title = models.CharField(max_length=700)
    genre = models.CharField(max_length=200)
    album_image = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    '''The Song model which creates tables in the database for song objects storage'''
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title