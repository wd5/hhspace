# -*- coding: utf8 -*-

from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.forms.models import save_instance
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template
from account.forms import MessageForm, MessageReplyForm
from account.models import Singer, CustomUser, Message
from utils.views import edit_url


def object_list(request, is_read = None):

    id = request.user.id
    try:
        profile = Singer.objects.get(customuser_ptr=id)
    except Singer.DoesNotExist:
        profile = CustomUser.objects.get(pk=request.id)
    nnation_tab = 'active'

    if is_read is None:
        msgs = Message.objects.filter(to__pk=id)
    else:
        msgs = Message.objects.filter(to__pk=id).filter(is_read=is_read)

    return direct_to_template(request, 'message/list.html', locals() )

def object_view(request, message_id):

    c = {}
    csrf(request)

    id = request.user.id
    try:
        profile = Singer.objects.get(customuser_ptr=id)
    except Singer.DoesNotExist:
        profile = CustomUser.objects.get(pk=request.id)

    message = get_object_or_404(Message, pk=message_id)
    nnation_tab = 'active'
    form = MessageReplyForm(initial={'theme': 'Re: %s' % message.theme, 'to_id' : message.ffrom_id})
    to = message.ffrom_id

    message.is_read = 1
    message.save()

    return direct_to_template(request, 'message/view.html', locals(),  context_instance=RequestContext(request))

def object_edit(request):

    csrf(request)
    id = request.user.id
    try:
        profile = Singer.objects.get(customuser_ptr=id)
    except Singer.DoesNotExist:
        profile = CustomUser.objects.get(pk=request.id)
    nnation_tab = 'active'
    user = profile

    if not request.POST:
        form = MessageForm()
        return render_to_response('message/edit.html', locals(),  context_instance=RequestContext(request))
    else:
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = Message()
            message.ffrom_id = request.user.id

            ids = request.POST.getlist('to_id')
            for idx,to in enumerate(ids):
                message.to_id = to
                save_instance(form, message)
                
            return HttpResponseRedirect(reverse('message_send'))
        else:
            return render_to_response('message/edit.html', locals(), context_instance=RequestContext(request))

def message_reply(request, to):

    csrf(request)
    id = request.user.id
    try:
        profile = Singer.objects.get(customuser_ptr=id)
    except Singer.DoesNotExist:
        profile = CustomUser.objects.get(pk=request.id)
    nnation_tab = 'active'
    user = profile

    if not request.POST:
        form = MessageReplyForm(initial={'to_id' : to})
        return render_to_response('message/reply.html', locals(),  context_instance=RequestContext(request))
    else:
        form = MessageReplyForm(request.POST, request.FILES)
        if form.is_valid():
            message = Message()
            message.to_id = request.POST['to_id']
            message.ffrom_id = request.user.id
            save_instance(form, message)

            return HttpResponseRedirect(reverse('message_send'))
        else:
            return render_to_response('message/reply.html', locals(), context_instance=RequestContext(request))

def message_send(request):

    id = request.user.id
    try:
        profile = Singer.objects.get(customuser_ptr=id)
    except Singer.DoesNotExist:
        profile = CustomUser.objects.get(pk=request.id)
    nnation_tab = 'active'
    user = profile
    
    return render_to_response('message/send.html', locals())

