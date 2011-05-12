# -*- coding: utf8 -*-
from discography.models import SingerAlbum, TrackSingerAblum
from django import forms

class SingerAlbumForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    
    class Meta:
        model = SingerAlbum
        exclude = ('singer')

    def save(self, singer_id):
        obj = super(SingerAlbumForm, self).save(commit=False)
        obj.singer_id = singer_id
        obj.save()
        return obj

class SingerTrackForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')

    class Meta:
        model = TrackSingerAblum
        exclude = ('album')

    def save(self, album_id):
        obj = super(SingerTrackForm, self).save(commit=False)
        obj.album_id = album_id
        obj.save()
        return obj


    
