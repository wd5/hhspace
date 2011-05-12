from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.account.views',
                       (r'^\d{1,2}$', 'account'),
                       ('^logout/$', 'logout_view'),
                       ('^login/$', 'user_login_view'),
                       ('^biography/$', 'biography_view'),
                       ('^biography/edit/$', 'biography_edit')
)
