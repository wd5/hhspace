# -*- coding: utf8 -*-
import datetime
from django.db import models
from django.db.models import permalink
from account.models import Singer,  Style, Direction, CustomUser
from customuser.models import City, Region, Country
from hhspace.discography.models import Album, Track
from hhspace.photoalbum.models import Photoalbum, PhotoComment, Photo
from hhspace.video.models import Video
from hhspace.audio.models import Audio

class Group(models.Model):
    name = models.CharField(max_length=150, unique=True)
    directions = models.ManyToManyField(Direction)
    styles = models.ManyToManyField(Style)
    country  = models.ForeignKey(Country)
    region = models.ForeignKey(Region)
    city = models.ForeignKey(City)
    # category = models.ForeignKey(Category)
    singers = models.ManyToManyField(Singer, through='Membership')
    leaders = models.CommaSeparatedIntegerField(blank=True, max_length=255)
    date_created = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    featuring = models.IntegerField(default = 0)
    last_visit = models.DateTimeField(auto_created=True,auto_now=True)
    timestamp = models.DateTimeField(auto_now=True, default=datetime.datetime.now())
    image = models.ImageField(upload_to='group')

    status = models.CharField(max_length=50, blank=True, default='Online')
    mood = models.CharField(max_length=50, blank=True, default='Отпад')

    biography = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('group_view', None, {'group_id' : self.pk})

    def isleader(self, id):
        return id == int(self.leaders)
    
    def username(self):
        return self.name

    def issinger(self):
        return True

    def get_username(self):
        return self.name

    def get_avatar_thumb(self):
        return self.image

    def get_avatar_mainthumb(self):
        return self.image

    def get_avatar(self):
        return self.image

class Membership(models.Model):
    singer = models.ForeignKey(Singer)
    group = models.ForeignKey(Group)
    date_joined = models.DateField(blank=True, auto_now=True)
    invite_reason = models.CharField(max_length=160, blank=True, verbose_name='Причина')

    def __unicode__(self):
        return '%s, %s %s'% (self.group.name, self.singer.first_name, self.singer.last_name)



class GroupAlbum(Album):
    group = models.ForeignKey(Group)

    @permalink
    def get_absolute_url(self):
        return ('group_discography_view', None, {'group_id' : self.group_id, 'album_id' : self.id})


class TrackGroupAblum(Track):
    album = models.ForeignKey(GroupAlbum)

class PhotoAlbum(Photoalbum):
    group = models.ForeignKey(Group, null=False)

    @permalink
    def get_absolute_url(self):
        return ('group_photoalbum_view', None, {'group_id': self.group.pk, 'album_id' : self.id})

class Photo(Photo):
    album = models.ForeignKey(PhotoAlbum, null=False)

    @permalink
    def get_absolute_url(self):
        return ('group_photo_view', None, {'group_id': self.album.group.pk, 'album_id' : self.album.pk, 'photo_id' : self.id})

class PhotoComment(PhotoComment):
    user = models.ForeignKey(CustomUser, null=False, default=1,  related_name='group_photocomment_set', )
    photo = models.ForeignKey(Photo, null=False, default=1)

class Video(Video):
    group = models.ForeignKey(Group, default=1)

    @permalink
    def get_absolute_url(self):
        return ('group_video_add', None, { 'group_id' : self.group_id, 'video_id' : self.id})

class Audio(Audio):
    group = models.ForeignKey(Group, default=1)

    @permalink
    def get_absolute_url(self):
        return ('group_audio_view', None, { 'group_id' : self.group_id, 'audio_id' : self.id})


class BookmarkGroup(models.Model):
    user = models.ForeignKey(CustomUser, default=1, related_name='bookmarks_groups')
    mark = models.ForeignKey(Group, default=1, related_name='mark_groups')
    date = models.DateTimeField(auto_now=True, blank=True)