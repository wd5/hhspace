# -*- coding: utf8 -*-
from datetime import datetime
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=150, default='', null=False)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='albums', verbose_name=u'Фото', null=False)
    city = models.CharField(max_length=150, default='', null=False)
    year = models.CharField(max_length=150, default='', null=False)
    date_creation = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateField(auto_now=True, blank=True)

    
    class Meta:
        abstract = True
        ordering = ['date_update']

    def __unicode__(self):
        return '%s'% self.name


class Track(models.Model):
    name = models.CharField(max_length=150, default='', null=False)
    description = models.TextField(default='')
    city = models.CharField(max_length=150, default='', null=False)
    music_by = models.CharField(max_length=150, default='', null=False)
    perform_by = models.CharField(max_length=150, default='', null=False)
    right_to = models.CharField(max_length=150, default='', null=False)
    year = models.PositiveIntegerField(default=2012)
    duration = models.CharField(max_length=10, default='', null=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
