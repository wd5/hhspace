from datetime import datetime
from django.db import models

class Photoalbum(models.Model):
    name = models.CharField(max_length=150, null=False)
    date_created = models.DateField(auto_now_add=True,  null=False)
    date_updated = models.DateTimeField(auto_now=True,  null=False)
    year = models.PositiveIntegerField(null=False, default=2011)
    city = models.CharField(max_length=150, null=False)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-date_updated']


class Photo(models.Model):
    name = models.CharField(max_length=150, null=False)
    visited = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to='photos', null=False)
    description = models.CharField(max_length=250, null=False, default='')
    date_created = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['-id']

        
class PhotoComment(models.Model):
    title = models.CharField(max_length=150, null=False, default='')
    date_created = models.DateTimeField(auto_now=True, auto_now_add=True, null=False, default=str(datetime.now())[0:10])
    text = models.TextField(null=False, default='')

    class Meta:
        abstract = True
        ordering = ['-id']


        
