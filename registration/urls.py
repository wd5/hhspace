"""
URLConf for Django user registration and authentication.

Recommended usage is a call to ``include()`` in your project's root
URLConf to include this URLConf for any URL beginning with
``/accounts/``.

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       (r'^$', 'registration.views.register'),
                       (r'^group/$', 'registration.views.register_group'),
                       ('^complete/$', direct_to_template, {
                            'template' : 'registration/complete.html'
                        }),
                       ('^group/complete/$', direct_to_template, {
                            'template' : 'registration/group_complite.html'
                        }),
)
