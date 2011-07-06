from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'hhspace.customuser.views.main', name='mainpage'),
    url('^singer/ajax_list/$', 'hhspace.account.views.ajax_singer_list', name='ajax_singer_list'),
    url('^style/ajax_list/$', 'hhspace.account.views.ajax_style_list', name='ajax_style_list'),
    
    (r'^registration/', include('hhspace.registration.urls')),
    url('^account/', include('hhspace.account.urls')),
    url('^user/', include('hhspace.customuser.urls')),
    url('^group/', include('hhspace.group.urls')),
    url('^news/', include('hhspace.content.urls')),
    url('^account/(?P<id>\d+)/group/', include('hhspace.group.urls')),
    url('^video/progress/$', 'hhspace.video.views.video_upload_progress', name="video_upload_progress"),
    url('^audio/progress/$', 'hhspace.audio.views.audio_upload_progress', name="audio_upload_progress"),

    (r'^admin/', include(admin.site.urls)),
    (r'^avatar/', include('hhspace.avatar.urls')),
    (r'^test/', direct_to_template, {
        'template' : 'test.html',
    }),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
    ),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),

)
