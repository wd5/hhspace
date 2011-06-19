# -*- coding: utf8 -*-
from django.utils.html import linebreaks
from account.models import CustomUser, TrackSingerAblum, SingerAlbum, Photo, PhotoComment, PhotoAlbum, Video, Audio
from django import forms
import hhspace

class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Имя')
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Фамилия')
    street = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Улица')
    index = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Индекс')
    #country  = models.ForeignKey(Country, default=1, verbose_name='Страна')
    #region = models.ForeignKey(Region, default=1, verbose_name='Регион')
    #city = models.ForeignKey(City, default=1, verbose_name='Город')
    status = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Статус')
    mood = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Настроение')
    url = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Сайт')
    birthday = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'День рождения')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'street', 'index', 'status', 'mood', 'url', 'birthday', )

    def save(self):
        obj = super(ProfileForm, self).save(commit=False)
        return obj.save()

class UserProfileForm(forms.ModelForm):

    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Псевдоним')
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Имя')
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Фамилия')
    #country  = models.ForeignKey(Country, default=1, verbose_name='Страна')
    #region = models.ForeignKey(Region, default=1, verbose_name='Регион')
    #city = models.ForeignKey(City, default=1, verbose_name='Город')
    status = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Статус')
    mood = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Настроение')
    url = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Сайт')
    birthday = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'День рождения')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',  'status', 'mood', 'url', 'birthday', )

    def save(self):
        obj = super(UserProfileForm, self).save(commit=False)
        return obj.save()

class BiographyForm(forms.ModelForm):

    biography = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class':'field'}), label = 'Биография  ')

    class Meta:
        model = CustomUser
        fields = ('biography', )

    def save(self):
        obj = super(BiographyForm, self).save(commit=False)
        obj.biography = obj.biography.replace('\n','<br />')
        return obj.save()


class SingerAlbumForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    description = forms.CharField(widget=forms.Textarea(), required=False, label = u'Описание')
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Город')

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
    music_by = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Автор музыки')
    city = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Город')
    perform_by = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Автор')
    right_to = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Права')
    year = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Год')

    class Meta:
        model = TrackSingerAblum
        exclude = ('album')
        fields = ('name', 'perform_by', 'music_by', 'city', 'right_to', 'year')

    def save(self, album_id):
        obj = super(SingerTrackForm, self).save(commit=False)
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

    def save(self, singer_id):
        obj = super(PhotoAlbumForm, self).save(commit=False)
        obj.singer_id = singer_id
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
        choices=yearchoise,
        label = u'Год'
        )

    class Meta:
        model = Audio
        fields = ('audio', 'artist', 'music_author', 'words_author', 'year', 'right_to', 'description', )

    def save(self):
        obj = super(AudioForm, self).save(commit=False)
        return obj.save()