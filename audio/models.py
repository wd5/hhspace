# -*- coding: utf8 -*-
from datetime import datetime
import logging
import os
from django.conf import settings
from django.core.cache import cache
from django.core.files.uploadhandler import MemoryFileUploadHandler
from django.db import models
from django.template.defaultfilters import filesizeformat
from django.core.files import storage 

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

class FileSystemStorage(storage.FileSystemStorage):
    """
    Subclass Django's standard FileSystemStorage to fix permissions
    of uploaded files.
    """
    def _save(self, name, content):
       name =  super(FileSystemStorage, self)._save(name, content)
       full_path = self.path(name)
       mode = getattr(settings, 'FILE_UPLOAD_PERMISSIONS', None)
       if not mode:
           mode = 0644
       os.chmod(full_path, mode)                                                                                                                                                    
       return name

class Audio(models.Model):
    artist = models.CharField(max_length=150, verbose_name='Исполнитель')
    music_author = models.CharField(max_length=150, blank=True, verbose_name=u'Автор музыки', default='')
    words_author = models.CharField(max_length=150, blank=True, verbose_name=u'Автор слов', default='')
    year = models.PositiveIntegerField(default=2000, choices=yearchoise, verbose_name=u'Год')
    right_to = models.CharField(max_length=150, blank=True, verbose_name=u'Права', default='')
    description = models.TextField(default="", verbose_name=u'Описание')
    name = models.CharField(max_length=150, blank=True, verbose_name=u'Название', default='')
    order = models.PositiveIntegerField(default=1)
    audio = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='audio', verbose_name=u'Загрузить файл', default='')
    timestamp = models.DateTimeField(default=datetime.now, auto_now_add=True)
    # user = models.ForeignKey(CustomUser, default=1)

    class Meta:
        abstract = True
        ordering = ['-timestamp', 'order']

    def __unicode__(self):
        return u"%s - %s" % (self.artist, self.name )

    @property
    def size(self):
        return filesizeformat(self.audio.size)


class UploadProgressCachedHandler(MemoryFileUploadHandler):
    """
    Tracks progress for file uploads.
    The http post request must contain a query parameter, 'X-Progress-ID',
    which should contain a unique string to identify the upload to be tracked.
    """

    def __init__(self, request=None):
        super(UploadProgressCachedHandler, self).__init__(request)
        self.progress_id = None
        self.cache_key = None

    def handle_raw_input(self, input_data, META, content_length, boundary, encoding=None):
        self.content_length = content_length
        if 'X-Progress-ID' in self.request.GET:
            self.progress_id = self.request.GET['X-Progress-ID']
        if self.progress_id:
            self.cache_key = "%s_%s" % (self.request.META['REMOTE_ADDR'], self.progress_id )
            cache.set(self.cache_key, {
                'state': 'uploading',
                'size': self.content_length,
                'received': 0
            })
            if settings.DEBUG:
                logging.debug('Initialized cache with %s' % cache.get(self.cache_key))
        else:
            logging.getLogger('UploadProgressCachedHandler').error("No progress ID.")

    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        pass

    def receive_data_chunk(self, raw_data, start):
        if self.cache_key:
            data = cache.get(self.cache_key)
            if data:
                data['received'] += self.chunk_size
                cache.set(self.cache_key, data)
                if settings.DEBUG:
                    logging.debug('Updated cache with %s' % data)
        return raw_data

    def file_complete(self, file_size):
        pass

    def upload_complete(self):
        if settings.DEBUG:
            logging.debug('Upload complete for %s' % self.cache_key)
        if self.cache_key:
            cache.delete(self.cache_key)