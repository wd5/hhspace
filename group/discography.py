# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from hhspace.group.forms import GroupAlbumForm, GroupTrackForm
from hhspace.group.models import Group, GroupAlbum, TrackGroupAblum

# ToDo
# сделать проверку на соотвествение человека в руководителях группы
from utils.views import edit_url

def discography_list(request, group_id):
    profile = Group.objects.get(pk=group_id)

    try:
        albums = GroupAlbum.objects.filter(group=profile)
    except GroupAlbum.DoesNotExist:
        albums = {}

    disco_tab = 'active'
    editurl = edit_url(request.user, profile, "discography_add", [profile.id])

    return direct_to_template(request, 'discography/album_list.html', locals() )

def discography_view(request, group_id, album_id):

    album = get_object_or_404(GroupAlbum, pk=album_id)
    profile = get_object_or_404(Group, pk=group_id)
    disco_tab = 'active'

    editurl = edit_url(request.user, profile, "track_edit", [profile.id, album_id])

    try:
        tracks = TrackGroupAblum.objects.filter(album=album_id)
    except TrackGroupAblum.DoesNotExist:
        tracks = {}

    return direct_to_template(request, 'discography/album.html', locals() )

@login_required(login_url='/user/login/')
def album_edit(request, group_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = Group.objects.get(pk=group_id)
    c['disco_tab'] = 'active'
    c['formurl']  = edit_url(request.user, c['profile'], "discography_add", [c['profile'].id], 0)

    # ToDo
    # сделать проверку на соотвествение человека в руководителях группы

    if not request.POST:
        form = GroupAlbumForm()
        c['form'] = form
        return render_to_response('discography/album_edit.html', c)
    else:
        form = GroupAlbumForm(request.POST,  request.FILES)
        if form.is_valid():
            album = form.save(group_id)
            return HttpResponseRedirect(reverse('group_discography_view', args=[group_id, album.pk]))
        else:
            form = GroupAlbumForm(request.POST, request.FILES)
            c['form'] = form
            return render_to_response('discography/album_edit.html', c)

@login_required(login_url='/user/login/')
def track_edit(request, album_id, group_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = get_object_or_404(Group, pk=group_id)
    album = GroupAlbum.objects.get(pk=album_id)
    c['album'] = album
    c['disco_tab'] = 'active'
    c['formurl']  = edit_url(request.user, c['profile'], "track_edit", [c['profile'].id, album_id], 0)

    if not request.POST:
        form = GroupTrackForm()
        c['form'] = form
        return render_to_response('discography/track_edit.html', c)
    else:
        form = GroupTrackForm(request.POST)
        if form.is_valid():
            track = form.save(album_id)
            return HttpResponseRedirect(reverse('group_discography_view', args=[group_id, album.pk]))
        else:
            form = GroupTrackForm(request.POST)
            c['form'] = form
            return render_to_response('discography/track_edit.html', c)