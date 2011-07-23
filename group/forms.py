# -*- coding: utf8 -*-
from django import forms
from django.core.urlresolvers import reverse
from django.forms.extras.widgets import SelectDateWidget
from account.models import Singer
from group.models import Group,TrackGroupAblum, GroupAlbum, Photo, PhotoAlbum, PhotoComment, Video, Audio
from hhspace.utils.autocomplete import ModelAutoCompleteField

MUSIC_YEARS = map(lambda a: (a,a), range(2000, 2012))
class GroupForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Название'
    )
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Название'
    )
    # date_created = forms.DateField(widget=SelectDateWidget(attrs={'class' : 'sel-small'},), label=_(u'Дата начала деятельности'))
    invite = ModelAutoCompleteField(lookup_url = '/singer/ajax_list/',
                                    model = Singer, required=False, label=u'Участники')

    class Meta:
        model = Group
        fields = ('name', 'image', 'country', 'region', 'city', 'directions', 'styles', 'invite'  )

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
        obj.biography = obj.biography.replace('\n','<br />')
        return obj.save()



class GroupAlbumForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    description = forms.CharField(widget=forms.Textarea(), required=False, label = u'Описание')
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Город')
    year = forms.ChoiceField(choices=MUSIC_YEARS, widget=forms.Select(attrs={'class':'field'}), label = 'Год')

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
    year = forms.ChoiceField(choices=MUSIC_YEARS,  widget=forms.Select(attrs={'class':'field'}), label = 'Год')

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
    description = forms.CharField(max_length=250, widget=forms.Textarea(), label='Описание')

    class Meta:
        model = PhotoAlbum
        fields = ('name', 'city', 'year', 'description', )
        exclude = ('singer')

    def save(self, group_id):
        obj = super(PhotoAlbumForm, self).save(commit=False)
        obj.group_id = group_id
        obj.save()
        return obj

class PhotoForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название', required=False)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea(), label='Описание', required=False)

    class Meta:
        model = Photo
        fields = ('name', 'image', 'description')

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
        choices=MUSIC_YEARS,
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

class AudioForm(forms.ModelForm):

    artist = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Исполнитель'

    )
    music_author = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Автор музыки'
    )
    words_author = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Автор слов'
    )
    right_to = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', 'style' : 'width: 168px'}),
        label = u'Права'
    )
    description = forms.CharField(widget=forms.Textarea(), required=False, label = u'Описание')
    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class' : 'field', }),
        label = u'Название'
    )
    year = forms.ChoiceField(
        widget=forms.Select(attrs={'class' : 'sel-data'}),
        choices=MUSIC_YEARS,
        label = u'Год'
        )

    class Meta:
        model = Audio
        fields = ('audio', 'artist', 'music_author', 'words_author', 'year', 'right_to', 'description', )

    def save(self):
        obj = super(AudioForm, self).save(commit=False)
        return obj.save()    