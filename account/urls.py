from django.conf.urls.defaults import *

from hhspace.registration.views import logout_view
from hhspace.registration.views import user_login_view

urlpatterns = patterns('',
                       url('^logout/$', logout_view),
                       url('^login/$', user_login_view),
)
