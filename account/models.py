# -*- coding: utf8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models import permalink
import hhspace
from hhspace.avatar.settings import AVATAR_DEFAULT_URL
from hhspace.settings import MEDIA_URL
from hhspace.discography.models import Album, Track
from hhspace.photoalbum.models import Photo, Photoalbum, PhotoComment
from hhspace.video.models import Video
from hhspace.audio.models import Audio

SEX_CHOICES = (
        (True, 'Male'),
        (False, 'Female')
)

class Direction(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_photo(self):
        try:
            return hhspace.account.models.Photo.objects.filter(album__singer__directions__id=self.id)[0]
        except IndexError, e:
            return ''

    def get_singer(self):
        try:
            return Singer.objects.filter(directions__id=self.id)[0]
        except IndexError, e:
            return ''

    def get_video(self):
        try:
            return hhspace.account.models.Video.objects.filter(singer__directions__id=self.id)[0]
        except IndexError, e:
            return ''

class Style(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'styles'

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'countries'

class Region(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'Город')
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'cities'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class CustomUser(User):

    country  = models.ForeignKey(Country, default=1, verbose_name='Страна')
    region = models.ForeignKey(Region, default=1, verbose_name='Регион')
    city = models.ForeignKey(City, default=1, verbose_name='Город')
    sex = models.BooleanField(default=True, choices=SEX_CHOICES, verbose_name='Пол')
    status = models.CharField(max_length=50, blank=True, default='')
    mood = models.CharField(max_length=50, blank=True, default='')
    url = models.URLField(max_length=100, blank=True, default='')
    birthday = models.DateTimeField(blank=True, default=datetime.now, auto_created=True)

    biography = models.TextField(blank=True, default='')

    objects = UserManager()

    def get_avatar_thumb(self):
        try:
            return self.avatar_set.filter().order_by('-primary')[0].avatar_url(90)
        except IndexError:
            return MEDIA_URL + AVATAR_DEFAULT_URL

    def get_avatar_mainthumb(self):
        try:
            return self.avatar_set.filter().order_by('-primary')[0].avatar_url(110)
        except IndexError:
            return MEDIA_URL + AVATAR_DEFAULT_URL


    def get_avatar(self):
        try:
            return self.avatar_set.filter().order_by('-primary')[0].avatar_url(163)
        except IndexError:
            return MEDIA_URL + AVATAR_DEFAULT_URL

    def issinger(self):
        return False

    def get_username(self):
        if self.username:
            return self.username
        else:
            return self.first_name

    @permalink
    def get_absolute_url(self):
        return ('hhspace.account.views.account', None, {'id' : self.id})
    

class Singer(CustomUser):
    directions = models.ManyToManyField(Direction)
    # category = models.ForeignKey(Category)
    styles = models.ManyToManyField(Style, verbose_name='styles')
    featuring = models.IntegerField(default = 0)
    date_created = models.DateField(blank=True),
    street = models.CharField(max_length=100, blank=True),
    index = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return "%s %s"% (self.last_name, self.first_name)

    def issinger(self):
        return True


class SingerAlbum(Album):
    singer = models.ForeignKey('Singer')

    @permalink
    def get_absolute_url(self):
        return ('singer_discography_view', None, {'singer_id' : self.singer_id, 'album_id' : self.id})

class TrackSingerAblum(Track):
    album = models.ForeignKey('SingerAlbum')

class PhotoAlbum(Photoalbum):
    singer = models.ForeignKey(Singer, null=False)

    @permalink
    def get_absolute_url(self):
        return ('singer_photoalbum_view', None, {'singer_id': self.singer.pk, 'album_id' : self.id})

class Photo(Photo):
    album = models.ForeignKey(PhotoAlbum, null=False)

    @permalink
    def get_absolute_url(self):
        return ('singer_photo_view', None, {'singer_id': self.album.singer.pk, 'album_id' : self.album.pk, 'photo_id' : self.id})

class PhotoComment(PhotoComment):
    user = models.ForeignKey(CustomUser, null=False, default=1, related_name='singer_photocomment_set')
    photo = models.ForeignKey(Photo, null=False, default=1)

class Video(Video):
    singer = models.ForeignKey(Singer, default=1)

    @permalink
    def get_absolute_url(self):
        return ('singer_video_view', None, { 'singer_id' : self.singer_id, 'video_id' : self.id})

class Audio(Audio):
    singer = models.ForeignKey(Singer, default=1)

    @permalink
    def get_absolute_url(self):
        return ('singer_audio_view', None, { 'singer_id' : self.singer_id, 'audio_id' : self.id})