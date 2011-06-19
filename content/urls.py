from django.conf.urls.defaults import *

urlpatterns = patterns('hhspace.content.views',
                       url('^(?P<news_id>\d+)/$', 'news_show', name='news_show'),
                       url('^/$', 'news_list', name='news_list')
)