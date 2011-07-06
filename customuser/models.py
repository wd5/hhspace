# -*- coding: utf8 -*-
from datetime import datetime
from django.contrib.auth.models import UserManager, User
from django.db import models
from django.db.models import permalink
from avatar.settings import AVATAR_DEFAULT_URL
from settings import MEDIA_URL

SEX_CHOICES = (
        (True, 'Male'),
        (False, 'Female')
)


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


class CustomUser(User):

    country  = models.ForeignKey(Country, default=1, verbose_name='Страна')
    region = models.ForeignKey(Region, default=1, verbose_name='Регион')
    city = models.ForeignKey(City, default=1, verbose_name='Город')
    sex = models.BooleanField(default=True, choices=SEX_CHOICES, verbose_name='Пол')
    status = models.CharField(max_length=50, blank=True, default='Online')
    mood = models.CharField(max_length=50, blank=True, default='Отпад')
    url = models.URLField(max_length=100, blank=True, default='')
    birthday = models.DateTimeField(blank=True, default=datetime.now, auto_created=True, null=True)

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
        if self.username.__len__():
            return self.username
        else:
            return self.first_name

    @permalink
    def get_absolute_url(self):
        return ('hhspace.customuser.views.user', None, {'id' : self.id})

    def messages_new_count(self):
        return Message.objects.filter(to__id=self.pk).filter(is_read=0).count()

    def messages_count(self):
        return Message.objects.filter(to__id=self.pk).count()


class Message(models.Model):
    ffrom = models.ForeignKey(CustomUser, default=1, null=False, related_name='from_messages')
    to = models.ForeignKey(CustomUser, default=1, null=False, related_name='to_messages')
    theme = models.CharField(max_length=150, default='', null=False, verbose_name='Тема')
    message = models.TextField()
    is_read = models.BooleanField(default=0, null=False)
    date = models.DateTimeField(auto_now=True, blank=True, default=datetime.now)

    def __unicode__(self):
        return self.theme

    @permalink
    def get_absolute_url(self):
        return ('user_message_view', None, { 'message_id' : self.pk})

class BookmarkUser(models.Model):
    user = models.ForeignKey(CustomUser, default=1, related_name='bookmarks_users')
    mark = models.ForeignKey(CustomUser, default=1, related_name='mark_users')
    date = models.DateTimeField(auto_now=True, blank=True)