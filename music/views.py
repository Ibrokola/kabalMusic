from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import AlbumForm, SongForm

from .models import Album, Song



            #################
            ## Album Views ##
            #################

class AlbumCreateView(CreateView):
    '''The logic in this view creates the album'''
    model = Album





class AlbumDetailView(DetailView):
    '''The logic in this view gives the detail about the Album'''
    model = Album




class AlbumListView(ListView):
    '''The logic in this view lists the album'''
    model = Album




class AlbumDeleteView(DeleteView):
    '''The logic in this view deletes the album'''
    model = Album





            #################
            ## Song Views  ##
            #################

class SongCreateView(CreateView):
    '''The logic in this view creates the song'''
    model = Song




class SongListView(ListView):
    '''The logic in this view Lists the songs'''
    model = Song





class SongDetailView(DetailView):
    '''The logic in this view gives the detail about the Song'''
    model = Song





class SongDeleteView(DeleteView):
    '''The logic in this view deletes the album'''
    model = Song


