from django.conf.urls import url

from .views import (
                    AlbumCreateView,
                    AlbumDetailView,
                    AlbumDeleteView,
                    AlbumListView,
                    SongCreateView,
                    SongDetailView,
                    SongDeleteView,
                    SongListView,
                )



urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name='album_list'),
    url(r'^album_create/$', AlbumCreateView.as_view(), name='album_create'),
    url(r'^(?P<album_id>[0-9]+)/$', AlbumDetailView.as_view(), name='album_detail'),
    url(r'^(?P<album_id>[0-9]+)/album_delete/$', AlbumDeleteView.as_view(), name='album_delete'),
    
    url(r'^/(?P<album_id>[0-9]+)/song_create/$', SongCreateView.as_view(), name='song_create'),
    url(r'^/songs/(?P<filter_by>[a-zA_Z]+)/$', SongListView.as_view(), name='song_list'),
    url(r'^/(?P<album_id>[0-9]+)/delete_song/(?<song_id>[0-9]+)/$', SongDeleteView.as_view(), name='song_delete')
]
