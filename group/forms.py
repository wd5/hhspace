# -*- coding: utf8 -*-
from django import forms
from django.core.urlresolvers import reverse
from account.models import Singer
from group.models import Group,TrackGroupAblum, GroupAlbum, Photo, PhotoAlbum, PhotoComment, Video
from hhspace.utils.autocomplete import ModelAutoCompleteField

class GroupForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Название'

    )
    date_created = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Дата создания'
    )
    invite = ModelAutoCompleteField(lookup_url = '/singer/ajax_list/',
                                    model = Singer, required=False)

    class Meta:
        model = Group
        fields = ('name', 'date_created', 'country', 'region', 'city', 'directions', 'styles', 'invite'  )

    def save(self):
        obj = super(GroupForm, self).save(commit=False)
        return obj.save()

class GroupBiographyForm(forms.ModelForm):

    biography = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class':'field'}), label = 'Биография  ')

    class Meta:
        model = Group
        fields = ('biography', )

    def save(self):
        obj = super(GroupBiographyForm, self).save(commit=False)
        return obj.save()



class GroupAlbumForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    description = forms.CharField(widget=forms.Textarea(), required=False, label = u'Описание')
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Город')

    class Meta:
        model = GroupAlbum
        exclude = ('group')

    def save(self, group_id):
        obj = super(GroupAlbumForm, self).save(commit=False)
        obj.group_id = group_id
        obj.save()
        return obj

class GroupTrackForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    music_by = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Автор музыки')
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Город')
    perform_by = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Автор')
    right_to = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Права')
    year = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Год')

    class Meta:
        model = TrackGroupAblum
        exclude = ('album')
        fields = ('name', 'perform_by', 'music_by', 'city', 'right_to', 'year')

    def save(self, album_id):
        obj = super(GroupTrackForm, self).save(commit=False)
        obj.album_id = album_id
        obj.save()
        return obj

class PhotoAlbumForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Город', required=False)
    year = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Год', required=False)
    image = forms.ImageField()

    class Meta:
        model = PhotoAlbum
        fields = ('name', 'city', 'year', )
        exclude = ('singer')

    def save(self, group_id):
        obj = super(PhotoAlbumForm, self).save(commit=False)
        obj.group_id = group_id
        obj.save()
        return obj

class PhotoForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название', required=False)
    image = forms.ImageField()

    class Meta:
        model = Photo
        fields = ('name', 'image')

    def save(self, album_id):
        obj = super(PhotoForm, self).save(commit=False)
        obj.album_id = album_id
        obj.save()
        return obj

class CommentForm(forms.ModelForm):


    class Meta:
        model = PhotoComment
        fields = ('text', )

    def clean_photo(self):

        data = self.cleaned_data['photo']
        try:
            photo = PhotoComment.objects.get(pk=data)
            return photo
        except PhotoComment.DoesNotExist:
            raise forms.ValidationError("Photo doesn't exist")

    def save(self):
        obj = super(CommentForm, self).save(commit=False)
        return obj


yearchoise = (
    (2000, 2000),
    (2001, 2001),
    (2002, 2002),
    (2003, 2003),
    (2004, 2004),
    (2005, 2005),
    (2006, 2006),
    (2007, 2007),
    (2008, 2008),
    (2009, 2009),
    (2010, 2010),
    (2011, 2011),
)

class VideoForm(forms.ModelForm):

    artist = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Исполнитель'

    )
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Название'
    )
    director = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Режисер'
    )
    year = forms.ChoiceField(
        widget=forms.Select(attrs={'class' : 'sel-data'}),
        choices=yearchoise,
        label = u'Год'
        )
    city = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Город'
    )
    album = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', 'style' : 'width: 168px'}),
        label = u'Альбом'
    )
    description = forms.CharField(widget=forms.Textarea(), required=False, label = u'Описание')



    class Meta:
        model = Video
        fields = ('video', 'artist', 'name', 'director', 'year', 'city', 'album', 'description',  )

    def save(self):
        obj = super(VideoForm, self).save(commit=False)
        return obj.save()    