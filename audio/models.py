from django.db import models

yearchoise = (
    (2000, 2000),
    (2001, 2001),
    (2002, 2002),
    (2003, 2003),
    (2004, 2004),
    (2005, 2005),
    (2006, 2006),
    (2007, 2007),
    (2008, 2008),
    (2009, 2009),
    (2010, 2010),
    (2011, 2011),
)
class Audio(models.Model):
    artist = models.CharField(max_length=150)
    music_author = models.CharField(max_lenght=150, blank=True)
    words_author = models.CharField(max_lenght=150, blank=True)
    year = models.PositiveIntegerField(choices=yearchoise, defualt=2000)
    right_to = models.CharField(max_length=150, blank=True)
    description = models.TextField(default="")
    name = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=1)
    audio = models.FileField(upload_to='audio')
