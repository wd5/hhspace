from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.account.views',
                       url('^(?P<id>[\d]+)$', 'account', name='account'),
                       url('^(?P<singer_id>\d+)/biography/$', 'biography_view', name='singer_biography_view'),
                       url('^(?P<singer_id>\d+)/biography/edit/$', 'biography_edit', name='singer_biography_edit'),
                       url('^edit/$', 'object_edit', name='profile_edit'),
                       url('^(?P<param>\w+)/(?P<value>[\d]+)/$', 'account_list', name='account_list'),
)

urlpatterns += patterns('hhspace.account.discography',
                       url('^(?P<singer_id>\d+)/discography/(?P<album_id>\d+)/$', 'discography_view', name='singer_discography_view'),
                       url('^(?P<singer_id>\d+)/discography/edit/$', 'album_edit', name='singer_discography_add'),
                       url('^(?P<singer_id>\d+)/discography/(?P<album_id>\d+)/track/$', 'track_edit', name='singer_track_edit'),
                       url('^(?P<singer_id>\d+)/discography/$', 'discography_list', name='singer_discography_list'),
)

urlpatterns += patterns('hhspace.account.photoalbum',
                       url(r'^(?P<singer_id>\d+)/photoalbum/(?P<album_id>\d+)/photo/(?P<photo_id>\d+)/comment/add/$', 'album_view', name='singer_photoalbum_comment_add'),
                       url(r'^(?P<singer_id>\d+)/photoalbum/(?P<album_id>\d+)/$', 'album_view', name='singer_photoalbum_view'),
                       url(r'^(?P<singer_id>\d+)/photoalbum/(?P<album_id>\d+)/photo/(?P<photo_id>\d+)/$', 'album_view', name='singer_photo_view'),
                       url(r'^(?P<singer_id>\d+)/photoalbum/edit/$', 'album_edit', name='singer_photoalbum_add'),
                       url(r'^(?P<singer_id>\d+)/photoalbum/(?P<album_id>\d+)/photo/add/$', 'photo_edit', name='singer_photoalbum_photo_add'),
                       url(r'^(?P<singer_id>\d+)/photoalbum/$', 'album_list', name='singer_photoalbum_list'),
)

urlpatterns += patterns('hhspace.account.video',
                       url(r'^(?P<singer_id>\d+)/video/edit/$', 'object_edit', name='singer_video_add'),
                       url(r'^(?P<singer_id>\d+)/video/$', 'object_list', name='singer_video_list'),
                       url(r'^(?P<singer_id>\d+)/video/(?P<video_id>\d+)/$', 'object_show', name='singer_video_view'),
                       url(r'^(?P<singer_id>\d+)/video/upload/$', 'video_upload', name='singer_video_upload'),
)

urlpatterns += patterns('hhspace.account.audio',
                       url(r'^(?P<singer_id>\d+)/audio/edit/$', 'edit', name='singer_audio_add'),
                       url(r'^(?P<singer_id>\d+)/audio/$', 'list', name='singer_audio_list'),
                       url(r'^(?P<singer_id>\d+)/audio/upload/$', 'upload', name='singer_audio_upload'),
                       # url(r'^progress/$', 'audio_upload_progress', name="audio_upload_progress"),
)

