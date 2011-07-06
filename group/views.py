# -*- coding: utf8 -*-
from datetime import datetime
import logging
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.forms.models import save_instance
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from account.models import Singer, CustomUser
from group.forms import GroupBiographyForm
from group.models import Membership, Group, BookmarkGroup, PhotoAlbum
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
    try:
        albums = PhotoAlbum.objects.filter(group=profile).order_by('-date_updated')[:2]
    except PhotoAlbum.DoesNotExist:
        photoadd = 'добавить фото'
    photoaddurl = edit_url(request.user, profile, 'photoalbum_add', [profile.pk] )
    videoaddurl = edit_url(request.user, profile, 'video_add', [profile.pk] )
    groups = Group.objects.filter(directions__pk=profile.directions.all()[0].pk).exclude(pk=profile.pk)[:10]

    return render_to_response('group/show.html', locals() )


@login_required(login_url='/account/login/')
def object_edit(request, group_id = None):

    c = {}
    c.update(csrf(request))

    if group_id is not None:
        group = Group.objects.get(pk=group_id)
        c['url'] = reverse('group_edit', args=[group_id])
        c['form'] = GroupForm(instance=group)
    else:
        c['form'] = GroupForm()
        c['url'] = reverse  ('group_new')
        group = Group()
        
    c['profile'] = c['user'] = Singer.objects.get(pk=request.user.pk)

    if request.method == 'POST':

        if group_id:
            form = GroupForm(request.POST, request.FILES, instance=group)
        else:
            form = GroupForm(request.POST, request.FILES )
        if form.is_valid():

            # Todo
            # Разобраться с датой!
            # group.date_created = datetime.now().__str__()[:10]
            group.timestamp = datetime.now()
            group.leaders = request.user.id
            save_instance(form, group)

            member = Membership()
            member.group = group
            member.singer_id = request.user.id
            member.invite_reason = 'Auto'
            member.date_joined = datetime.now()
            member.save()

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

    return render_to_response('customuser/biography.html', locals())

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
        form = GroupBiographyForm(initial={'biography' : c['profile'].biography.replace('<br />','\n') })
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

def bookmark_add(request, id):

    if request.user.is_anonymous():
        return HttpResponse('Вам необходимо  <a href="/registration/">зарегистрироватся</a>')
    else:
        o = BookmarkGroup.objects.filter(Q(user__id=request.user.id)&Q(mark__id=id)).count()
        if o == 0:
            b = BookmarkGroup()
            b.user_id = request.user.id
            b.mark_id = id
            b.save()
        return HttpResponse('Добавленно')

def bookmark_list(request, id):

    users = BookmarkGroup.objects.filter(user__id=request.user.id)
    groups = BookmarkGroup.objects.filter(user__id=request.user.id)

    try:
        profile = Singer.objects.get(pk=request.user.id)
    except Singer.DoesNotExist:
        profile = get_object_or_404(CustomUser, pk=request.user.id)

    user = profile

    return render_to_response('bookmark/list.html', locals() )

def bookmark_remove(request, id):

    o = BookmarkGroup.objects.filter(Q(user__id=request.user.id)&Q(mark__id=id))[0].delete()
    return HttpResponse('Удалено')

def ajax_change(request, group_id):

    group = Group.objects.get(pk=group_id)
    group.__setattr__(request.GET['name'],request.GET['value']);
    group.save()
    return HttpResponse(request.GET['value'])