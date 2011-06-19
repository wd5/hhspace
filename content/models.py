from django.db import models
from django.db.models import permalink

class News(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, default = '', blank=True)
    text = models.TextField(default="")
    date_created = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @permalink
    def get_absolute_url(self):
        return ('news_show', None, {'news_id' : self.id})

    def __unicode__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, default = '', blank=True)
    text = models.TextField(default="")
    date_created = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @permalink
    def get_absolute_url(self):
        return ('event_show', None, {'event_id' : self.id})

    def __unicode__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(default="")
    date_created = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @permalink
    def get_absolute_url(self):
        return ('page_show', None, {'page_id' : self.id})

    def __unicode__(self):
        return self.title 