from django.db import models
from hhspace.account.models import Singer,Group

from django.db.models.fields.related import ForeignKey

class Album(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='albums')
    city = models.CharField(max_length=150)
    date_creation = models.DateField(blank=True, default='')
    date_update = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s'% self.name

class GroupAlbum(Album):
    group = ForeignKey(Group)

class SingerAlbum(Album):
    singer = ForeignKey(Singer)

class Track(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='')
    city = models.CharField(max_length=150)
    music_by = models.CharField(max_length=150)
    perform_by = models.CharField(max_length=150)
    right_to = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    duration = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

class TrackGroupAblum(Track):
    album = ForeignKey('GroupAlbum')

class TrackSingerAblum(Track):
    album = ForeignKey('SingerAlbum')