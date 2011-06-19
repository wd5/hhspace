# -*- coding: utf8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from content.models import News

def news_show(request, news_id):

    news = get_object_or_404(News, pk=news_id)
    user = request.user
    news_tab = 'active'

    return render_to_response('news/show.html', locals())

def news_list(request):

    user = request.user

    return render_to_response('news/show.html', locals())
