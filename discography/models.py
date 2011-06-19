# -*- coding: utf8 -*-
from datetime import datetime
from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='albums', verbose_name=u'Фото')
    city = models.CharField(max_length=150)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    
    class Meta:
        abstract = True
        ordering = ['date_update']

    def __unicode__(self):
        return '%s'% self.name


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
