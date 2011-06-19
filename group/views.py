# -*- coding: utf8 -*-
from datetime import datetime
import logging
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.forms.models import save_instance
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render_to_response, get_object_or_404
from account.models import Singer, CustomUser
from group.forms import GroupBiographyForm
from group.models import Membership, Group
from hhspace.group.forms import GroupForm
from utils.views import edit_url

def object_list(request, id = None):

    if id is None:
        id = request.user.id

    profile = Singer.objects.get(pk=id)
    user = request.user

    try:
        groups = Group.objects.filter(membership__singer=profile)
    except Group.DoesNotExist:
        groups = {}

    return render_to_response('group/list.html', locals() )



def object_view(request, group_id):

    profile = get_object_or_404(Group, pk=group_id)
    user = request.user
    home_tab = 'active'

    return render_to_response('group/show.html', locals() )



@login_required(login_url='/account/login/')
def object_edit(request):

    c = {}
    c.update(csrf(request))
    c['form'] = GroupForm()
    c['user'] = request.user

    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = Group()
            # Todo
            # Разобраться с датой!
            # group.date_created = datetime.now().__str__()[:10]
            group.timestamp = datetime.now()
            group.leaders = request.user.id
            logging.info("form, group is {0:>s}".format(group, form))
            save_instance(form, group)

            member = Membership()
            member.group = group
            member.singer_id = request.user.id
            member.invite_reason = 'Auto'
            member.date_joined = datetime.now()
            member.save()

            logging.info("POST singers is : %s" % request.POST)
            singers = request.POST.getlist('singers')

            for idx, singer_pk in enumerate(singers):
                member = Membership()
                member.group = group
                member.singer_id = singer_pk
                member.invite_reason = 'Auto'
                member.date_joined = datetime.now().__str__()[:10]
                member.save()
                logging.info("singer id is : %s, numeric : %s" % (singer_pk, singers[idx]))
    
            return HttpResponseRedirect(reverse('group_list'))
        else:
            c['form'] = form

    return render_to_response('group/edit.html', c)

def biography_view(request, group_id):

    profile = get_object_or_404(Group, pk=group_id)
    user = request.user
    biography_tab = 'active'
    editurl = edit_url(user, profile, "biography_edit", [group_id])

    return render_to_response('account/biography.html', locals())

def biography_edit(request, group_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = get_object_or_404(Group, pk=group_id)
    
    if c['profile'].isleader(request.user.id) == False:
        return HttpResponseForbidden()

    c['formurl'] = edit_url(c['user'], c['profile'], 'biography_edit', [c['profile'].pk], 0)
    c['biography_tab'] = 'active'

    if not request.POST:
        form = GroupBiographyForm()
        c['form'] = form
        return render_to_response('account/biography_edit.html', c)
    else:
        form = GroupBiographyForm(data=request.POST, instance=c['profile'])
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group_biography_view', args=[group_id]))
        else:
            form = GroupBiographyForm(request.POST)
            c['form'] = form
            return render_to_response('account/biography_edit.html', c)