# -*- coding: utf8 -*-
import logging
import os
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

import datetime
from django.forms import save_instance
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.views.generic.simple import direct_to_template
from group.forms import VideoForm
from group.models import Group, Video
import settings
from utils.views import edit_url


@login_required(login_url='/account/login/')
def object_edit(request, group_id):

    c = {}
    c.update(csrf(request))
    c['video_tab'] = 'active'
    c['form'] = VideoForm()
    c['user'] = request.user
    c['profile'] = get_object_or_404(Group, pk=group_id)
    c['formurl'] = edit_url(request.user, c['profile'], "video_add", [c['profile'].pk], 0)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            logging.info("Upload form is valid: %s" % form)
            video = Video()
            video.timestamp = datetime.datetime.now()
            video.group_id = group_id
            save_instance(form, video)
            return HttpResponseRedirect(reverse('group_video_list', args=[group_id]))
        else:
            c['form'] = form

    return render_to_response('video/edit.html', c)

def object_list(request, group_id):

    video_tab = 'active'
    profile = Group.objects.get(pk=group_id)
    user = request.user
    editurl = edit_url(request.user, profile, "video_add", [profile.pk])
    csrf(request)
    
    try:
        videos = Video.objects.filter(group=profile)
    except Video.DoesNotExist:
        videos = {}
        
        
    return direct_to_template(request, 'video/list.html', locals() )

def object_show(request, group_id, video_id):

    video_tab = 'active'

    video = get_object_or_404(Video, pk=video_id)
    profile = get_object_or_404(Group, pk=group_id)
    videos = Video.objects.filter(group=video.group)
    editurl = edit_url(request.user, profile, "video_add", [profile.pk])
    csrf(request)

    return direct_to_template(request, 'video/show.html', locals() )

@login_required(login_url='/account/login/')
def video_upload(request, group_id):

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video()
            video.timestamp = datetime.datetime.now()
            video.group_id = group_id
            video.order = request.POST.get('order', 0)
            video.converted = 0
            logging.info("Form is : %s" % form)
            save_instance(form, video)
            logging.info("Saved upload: %s" % video)
            request.user.message_set.create(message=_('Your file has been received.'))
        else:
            logging.error("invalid form: %s" % form)
            logging.error("form errors: %s" % form.errors)

    return HttpResponseRedirect(reverse('group_video_list', args=[group_id]))