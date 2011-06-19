# -*- coding: utf8 -*-
import logging
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.context_processors import csrf
from django.views.generic.simple import direct_to_template
from account.models import Singer, Audio
from account.forms import AudioForm

import datetime
from django.forms import save_instance
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

#Our initial page
from utils.views import edit_url

def initial(request):
	data = {
		'form': AudioForm(),
	}
	return render_to_response('audio/edit.html', data, RequestContext(request))
 

@login_required(login_url='/account/login/')
def edit(request, singer_id):

    c = {}
    c.update(csrf(request))
    c['audio_tab'] = 'active'
    c['form'] = AudioForm()
    c['user'] = request.user
    c['profile'] = get_object_or_404(Singer, pk = singer_id)
    c['formurl'] = edit_url(request.user, c['profile'], "audio_add", [c['profile'].pk], 0)
    c['nnation_tab'] = 'active'

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            logging.info("Upload form is valid: %s" % form)
            audio = Audio()
            audio.timestamp = datetime.datetime.now()
            audio.singer_id = request.user.id
            save_instance(form, audio)
            return HttpResponseRedirect(reverse('singer_audio_list', args=[singer_id]))
        else:
            c['form'] = form

    return render_to_response('audio/edit.html', c)

def list(request, singer_id):

    audio_tab = 'active'
    nnation_tab = 'active'
    profile = Singer.objects.get(pk=singer_id)
    editurl = edit_url(request.user, profile, "audio_add", [profile.pk])
    
    try:
        audios = Audio.objects.filter(singer=profile)
    except Audio.DoesNotExist:
        audios = {}
        
    return direct_to_template(request, 'audio/list.html', locals() )

@login_required(login_url='/account/login/')
def upload(request, singer_id):

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            audio = Audio()
            audio.timestamp = datetime.datetime.now()
            audio.user_id = singer_id
            audio.order = request.POST.get('order', 0)
            logging.info("Audio is : %s" % audio)

            save_instance(form, audio)
            logging.info("Saved upload: %s" % audio)
            request.user.message_set.create(message=_('Your file has been received.'))
        else:
            logging.error("invalid form: %s" % form)
            logging.error("form errors: %s" % form.errors)

    return HttpResponseRedirect(reverse('singer_audio_list', args=[singer_id]))
