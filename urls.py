from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.simple import direct_to_template
import settings

admin.autodiscover()

urlpatterns = patterns('',
    ('^$', direct_to_template, {
        'template' : 'index.html'
    }),
    (r'^registration/', include('hhspace.registration.urls')),
    url('^account/', include('hhspace.account.urls')),
    url('^discography/', include('hhspace.discography.urls')),
    url('^photoalbum/', include('hhspace.photoalbum.urls')),
    # Example:
    # (r'^hhspace/', include('hhspace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^avatar/', include('hhspace.avatar.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}
    ),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}
    ),

)
