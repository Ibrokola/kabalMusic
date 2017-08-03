from django import forms
from django.contrib.auth import settings

from .models import Album, Song

User = settings.AUTH_USER_MODEL

class AlbumForm(forms.ModelForm):
    '''Form for uploading Album details'''
    class Meta:
        '''Database table field directly from models'''
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_image']



class SongForm(forms.ModelForm):
    '''Form for uploading Songs'''
    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']