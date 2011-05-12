from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.discography.views',
                       (r'^album/(\d*)/$', 'album_view'),
                       ('^album/edit/$', 'album_edit'),
                       ('^track/add/album/(\d+)/$', 'track_edit'),
                       (r'^$', 'albumcollection_view'),
)   