from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.photoalbum.views',
                       (r'^album/(\d+)/$', 'album_view'),
                       (r'^album/edit/$', 'album_edit'),
                       (r'^photo/add/album/(\d+)/$', 'photo_edit'),
                       (r'^$', 'albums_view'),
)   