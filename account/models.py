from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.models import User, UserManager
from django.template.loader import render_to_string
import settings

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

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class CustomUser(User):

    country  = models.ForeignKey(Country, default=1)
    region = models.ForeignKey(Region, default=1)
    city = models.ForeignKey(City, default=1)
    sex = models.BooleanField(default=True, choices=SEX_CHOICES)
    status = models.CharField(max_length=50, blank=True, default='')
    mood = models.CharField(max_length=50, blank=True, default='')
    url = models.URLField(max_length=100, blank=True, default='')

    objects = UserManager()

class Singer(User):
    directions = models.ManyToManyField(Direction)
    category = models.ForeignKey(Category)
    styles = models.ManyToManyField(Style)
    featuring = models.IntegerField(default = 0)
    date_created = models.DateField(blank=True)

class Group(models.Model):
    name = models.CharField(max_length=150)
    directions = models.ManyToManyField(Direction)
    styles = models.ManyToManyField(Style)
    country  = models.ForeignKey(Country)
    region = models.ForeignKey(Region)
    city = models.ForeignKey(City)
    category = models.ForeignKey(Category)
    users = models.ManyToManyField(Singer)
    leaders = models.CommaSeparatedIntegerField(blank=True, max_length=255)
    date_created = models.DateField(blank=True)
    featuring = models.IntegerField(default = 0)
    last_login = models.DateTimeField(auto_created=True,auto_now=True)
    date_joined = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=50, blank=True)
    mood = models.CharField(max_length=50, blank=True)

# Create your models here.
