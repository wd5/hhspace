# -*- coding: utf8 -*-
from datetime import datetime
import logging
import os
from django.conf import settings
from django.core.cache import cache
from django.core.files.uploadhandler import MemoryFileUploadHandler
from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import filesizeformat
from django.core.files import storage
import settings

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

class Video(models.Model):
    video = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='video', verbose_name=u'Загрузить файл', default='')
    photo = models.CharField(max_length=250, default='', blank=True)
    flvvideo = models.CharField(max_length=250, default='', blank=True)
    artist = models.CharField(max_length=150, verbose_name='Исполнитель')
    name = models.CharField(max_length=150, blank=True, verbose_name=u'Название', default='')
    director = models.CharField(max_length=150, blank=True, verbose_name=u'Режисер', default='')
    year = models.PositiveIntegerField(default=2000, choices=yearchoise, verbose_name=u'Год')
    city = models.CharField(max_length=150, blank=True, verbose_name=u'Город', default='')
    album = models.CharField(max_length=150, blank=True, verbose_name=u'Альбом', default='')
    description = models.TextField(default="", verbose_name=u'Описание')
    timestamp = models.DateTimeField(default=datetime.now, auto_now_add=True)
    # singer = models.ForeignKey(Singer, default=1)
    converted = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['-timestamp', 'order']

    def __unicode__(self):
        return u"%s - %s" % (self.artist, self.name )

    @property
    def size(self):
        return filesizeformat(self.video.size)

    def convert(self):
        logging.info("Video name is : %s" % self.video.name)

        self.converted = 1
        self.save()
        
        self.flvvideo = 'media/' + self.video.name[:self.video.name.rfind('.')] + '.mp4'
        self.photo = 'media/' + self.video.name[:self.video.name.rfind('.')] + '.jpg'
        logging.info("Video is : %s" % self)


        os.system('%s -y -i "media/%s" -an -ss 21 -r 1 -vframes 1 -y -f mjpeg -s 150x130 "%s"' % (settings.patch.get('FFMPEG' or 'ffmpeg'), self.video.name, self.photo))
        logging.info('FFMPEG CONVERT: %s -i media/%s -threads 8  -vcodec libx264 -ar 22050 -ab 56k -vpre slow -aspect 4:3 -b 350k -r 12 -f mp4 -s 350x250 -acodec libfaac -ac 2 %s' % (settings.patch.get('FFMPEG' or 'ffmpeg'), self.video.name, self.flvvideo))
        os.system('%s -i media/%s -vcodec libx264 -ar 22050 -ab 56k -vpre slow -aspect 4:3 -b 350k -r 12 -f mp4 -s 480x230 -acodec libfaac -ac 2 %s' % (settings.patch.get('FFMPEG' or 'ffmpeg'), self.video.name, self.flvvideo))
        os.system('%s %s %s' % (settings.patch.get('QT-FASTSTART' or 'qt-faststart'), self.flvvideo, self.flvvideo))
        self.converted = 2

        self.save()


class VideoComment(models.Model):
    title = models.CharField(max_length=150, null=False, default='')
    date_created = models.DateTimeField(auto_now=True, auto_now_add=True, null=False, default=str(datetime.now())[0:10])
    text = models.TextField(default='')

    class Meta:
        abstract = True
        ordering = ['-id']

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
        else:
            logging.getLogger('UploadProgressCachedHandler').error("No progress ID.")

    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        pass

    def receive_data_chunk(self, raw_data, start):
        logger = logging.getLogger('uploaddemo.upload_handlers.UploadProgressCachedHandler.receive_data_chunk')
        if self.cache_key:
            data = cache.get(self.cache_key)
            if data:
                data['received'] += self.chunk_size
                cache.set(self.cache_key, data)
                if settings.DEBUG:
                    logger.debug('Updated cache with %s' % data)
        return raw_data

    def file_complete(self, file_size):
        pass

    def upload_complete(self):
        logger = logging.getLogger('uploaddemo.upload_handlers.UploadProgressCachedHandler.upload_complete')
        if settings.DEBUG:
            logger.debug('Upload complete for %s' % self.cache_key)
        if self.cache_key:
            cache.delete(self.cache_key)