from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.group.views',
                       url('^(?P<group_id>[\d]+)$', 'object_view', name='group_view'),
                       url('^edit/$', 'object_edit', name='group_new'),
                       url('^edit/(?P<group_id>\d+)/$', 'object_edit', name='group_edit'),
                       url('^list/$', 'object_list', name='group_list'),
                       url('^(?P<group_id>[\d]+)/biography/$', 'biography_view', name='group_biography_view'),
                       url('^(?P<group_id>[\d]+)/biography/edit/$', 'biography_edit', name='group_biography_edit'),
                       url('^(?P<id>\d+)/bookmark/add/', 'bookmark_add', name='group_bookmark_add'),
                       url('^(?P<id>\d+)/bookmark/remove/', 'bookmark_remove', name='group_bookmark_remove'),
                       url('^(?P<group_id>\d+)/ajax/change/', 'ajax_change', name='group_ajax_change')
)

urlpatterns += patterns('hhspace.group.discography',
                       url('^(?P<group_id>\d+)/discography/(?P<album_id>\d+)/$', 'discography_view', name='group_discography_view'),
                       url('^(?P<group_id>\d+)/discography/edit/$', 'album_edit', name='group_discography_add'),
                       url('^(?P<group_id>\d+)/discography/(?P<album_id>\d+)/track/$', 'track_edit', name='group_track_edit'),
                       url('^(?P<group_id>\d+)/discography/$', 'discography_list', name='group_discography_list'),
)

urlpatterns += patterns('hhspace.group.photoalbum',
                       url(r'^(?P<group_id>\d+)/photoalbum/(?P<album_id>\d+)/photo/(?P<photo_id>\d+)/comment/add/$', 'album_view', name='group_photoalbum_comment_add'),
                       url(r'^(?P<group_id>\d+)/photoalbum/(?P<album_id>\d+)/$', 'album_view', name='group_photoalbum_view'),
                       url(r'^(?P<group_id>\d+)/photoalbum/edit/$', 'album_edit', name='group_photoalbum_add'),
                       url(r'^(?P<group_id>\d+)/photoalbum/(?P<album_id>\d+)/photo/add/$', 'photo_edit', name='group_photoalbum_photo_add'),
                       url(r'^(?P<group_id>\d+)/photoalbum/$', 'album_list', name='group_photoalbum_list'),
)


urlpatterns += patterns('hhspace.group.video',
                       url(r'^(?P<group_id>\d+)/video/edit/$', 'object_edit', name='group_video_add'),
                       url(r'^(?P<group_id>\d+)/video/$', 'object_list', name='group_video_list'),
                       url(r'^(?P<group_id>\d+)/video/(?P<video_id>\d+)/$', 'object_show', name='group_video_show'),
                       url(r'^(?P<group_id>\d+)/video/upload/$', 'video_upload', name='group_video_upload'),
)
