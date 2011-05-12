# -*- coding: utf8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager


SEX_CHOICES = (
        (True, 'Male'),
        (False, 'Female')
)

class Direction(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

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
    birthday = models.DateField(blank=True, null=True)

    biography = models.TextField(blank=True, default='')

    objects = UserManager()

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

class Group(models.Model):
    name = models.CharField(max_length=150, unique=True)
    # directions = models.MaanyToManyField(Direction)
    styles = models.ManyToManyField(Style)
    country  = models.ForeignKey(Country)
    region = models.ForeignKey(Region)
    city = models.ForeignKey(City)
    # category = models.ForeignKey(Category)
    singers = models.ManyToManyField(Singer, through='Membership')
    leaders = models.CommaSeparatedIntegerField(blank=True, max_length=255)
    date_created = models.DateField(blank=True, verbose_name='Дата создания')
    featuring = models.IntegerField(default = 0)
    last_login = models.DateTimeField(auto_created=True,auto_now=True)
    date_joined = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=50, blank=True)
    mood = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name

class Membership(models.Model):
    singer = models.ForeignKey(Singer)
    group = models.ForeignKey(Group)
    date_joined = models.DateField(blank=True)
    invite_reason = models.CharField(max_length=160, blank=True, verbose_name='Причина')

    def __unicode__(self):
        return '%s, %s %s'% (self.group.name, self.user.first_name, self.user.last_name)

    
class News(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField(default="")
    date_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
