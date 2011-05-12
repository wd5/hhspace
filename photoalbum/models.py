from django.db import models
from account.models import Singer

class Photoalbum(models.Model):
    name = models.CharField(max_length=150)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)
    year = models.PositiveIntegerField()
    city = models.CharField(max_length=150)
    singer = models.ForeignKey(Singer)

class Photo(models.Model):
    name = models.CharField(max_length=150)
    visited = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to='photos')
    album = models.ForeignKey(Photoalbum)
    


