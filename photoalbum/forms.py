# -*- coding: utf8 -*-
from django import forms
from photoalbum.models import Photo, Photoalbum

class PhotoAlbumForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    
    class Meta:
        model = Photoalbum
        exclude = ('singer')

    def save(self, singer_id):
        obj = super(PhotoAlbumForm, self).save(commit=False)
        obj.singer_id = singer_id
        obj.save()
        return obj

class PhotoForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')

    class Meta:
        model = Photo
        exclude = ('album')

    def save(self, album_id):
        obj = super(PhotoForm, self).save(commit=False)
        obj.album_id = album_id
        obj.save()
        return obj


    
