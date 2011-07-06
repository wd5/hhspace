from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.customuser.views',
                       url('^(?P<id>[\d]+)$', 'user', name='user'),
                       url('^logout/$', 'logout_view', name='logout'),
                       url('^login/$', 'user_login_view', name='login'),
                       url('^(?P<user_id>\d+)/biography/$', 'biography_view', name='customuser_biography_view'),
                       url('^(?P<user_id>\d+)/biography/edit/$', 'biography_edit', name='customuser_biography_edit'),
                       url('^edit/$', 'object_edit', name='profile_edit'),
                       url('^(?P<param>\w+)/(?P<value>[\d]+)/$', 'user_list', name='customuser_list'),
                       url('^(?P<id>\d+)/bookmark/add/', 'bookmark_add', name='customuser_bookmark_add'),
                       url('^(?P<id>\d+)/bookmark/remove/', 'bookmark_remove', name='customuser_bookmark_remove'),
                       url('^(?P<id>\d+)/bookmark/list/', 'bookmark_list', name='bookmark_list'),
                       url('^(?P<user_id>\d+)/ajax/change/', 'ajax_change', name='customuser_ajax_change')
)

urlpatterns += patterns('hhspace.customuser.message',
                       url(r'^message/edit/$', 'object_edit', name='message_edit'),
                       url(r'^message/reply/(?P<to>\d+)/$', 'message_reply', name='message_reply'),
                       url(r'^message/list/$', 'object_list', name='message_list'),
                       url(r'^message/list/notread/$', 'object_list',{ 'is_read' : 0, },  name='message_list_new'),
                       url(r'^message/(?P<message_id>\d+)/view/$', 'object_view', name='message_view'),
                       url(r'^message/send/$', 'message_send', name='message_send'),
)