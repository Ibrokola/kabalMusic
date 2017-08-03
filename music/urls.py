from django.conf.urls import url

from .views import (
                    AlbumCreateView,
                    AlbumDetailView,
                    AlbumDeleteView,
                    AlbumListView,
                    SongCreateView,
                    SongDetailView,
                    SongDeleteView,
                )



urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name='album_list'),
    url(r'^album_create/$', AlbumCreateView.as_view(), name='album_create'),
    url(r'^(?P<album_id>[0-9]+)/$', AlbumDetailView.as_view(), name='album_detail'),
    url(r'^(?P<album_id>[0-9]+)/album_delete/$', AlbumDeleteView.as_view(), name='album_delete'),
    
]
