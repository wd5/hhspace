# -*- coding: utf8 -*-
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.forms.models import save_instance
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from group.models import Group, PhotoAlbum, Photo, PhotoComment
from group.forms import PhotoAlbumForm, CommentForm, PhotoForm
from utils.views import edit_url


def album_list(request, group_id):
    profile = Group.objects.get(pk=group_id)
    
    try:
        albums = PhotoAlbum.objects.filter(group=profile)
    except PhotoAlbum.DoesNotExist:
        albums = {}

    photo_tab = 'active'
    editurl = edit_url(request.user, profile, "photoalbum_add", [profile.pk])

    return direct_to_template(request, 'photoalbum/album_list.html', locals() )

def album_view(request, album_id, group_id, photo_id = None):

    c = {}
    c.update(csrf(request))
    c['photo_tab'] = 'active'
    c['profile'] = get_object_or_404(Group, pk=group_id)
    c['formurl']  = edit_url(request.user, c['profile'], "photoalbum_add", [c['profile'].pk], 0)
    c['edit_url'] = edit_url(request.user, c['profile'], "photoalbum_photo_add", [c['profile'].pk, album_id])


    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = PhotoComment()
            comment.photo_id = photo_id
            comment.user = request.user
            save_instance(form, comment)
            c['form'] = CommentForm()
        else:
            c['form'] = form
    else:
        c['form'] = CommentForm()
    try:
        photos = Photo.objects.filter(album=album_id)

        if photos.__len__() > 0:
            try:
                comments = PhotoComment.objects.filter(photo=photos[0])
            except PhotoComment.DoesNotExist:
                comments = {}
        else:
            comments = {}
    except Photo.DoesNotExist:
        photos = {}
        comments = {}

    c['album'] = PhotoAlbum.objects.get(pk=album_id)
    c['photos'] = photos
    c['user'] = request.user
    c['comments'] = comments
    c['commenturl'] = edit_url(request.user, c['profile'], 'photoalbum_comment_add', [c['profile'].pk, c['album'].pk, c['photos'][0].pk], 0)

    return direct_to_template(request, 'photoalbum/album.html', c )

@login_required(login_url='/user/login/')
def album_edit(request, group_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['photo_tab'] = 'active'
    c['profile'] = get_object_or_404(Group, pk=group_id)
    c['formurl']  = edit_url(request.user, c['profile'], "photoalbum_add", [c['profile'].pk], 0)

    if not request.POST:
        form = PhotoAlbumForm()
        c['form'] = form
        return render_to_response('photoalbum/album_edit.html', c)
    else:
        form = PhotoAlbumForm(request.POST, request.FILES)
        photoform = PhotoForm(request.POST, request.FILES)
        if form.is_valid() and photoform.is_valid():
            album = form.save(c['profile'].pk)
            photo = Photo()
            photo.album = album
            photo.description = request.POST.get('description', '')
            save_instance(photoform, photo)
                
            return HttpResponseRedirect(reverse('group_photoalbum_view', args=[c['profile'].pk, album.pk]))
        else:
            c['form'] = form
            return render_to_response('photoalbum/album_edit.html', c)

@login_required(login_url='/user/login/')
def photo_edit(request, group_id, album_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = get_object_or_404(Group, pk=group_id)
    album = PhotoAlbum.objects.get(pk=album_id)
    c['album'] = album
    c['photo_tab'] = 'active'
    c['formurl']  = edit_url(request.user, c['profile'], "photoalbum_photo_add", [c['profile'].pk, album.pk], 0)

    if not request.POST:
        form = PhotoForm()
        c['form'] = form
        return render_to_response('photoalbum/photo_edit.html', c)
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(album_id)
            return HttpResponseRedirect(reverse('group_photoalbum_view', args=[c['profile'].pk, album_id]))
        else:
            form = PhotoForm(request.POST, request.FILES)
            c['form'] = form
            return render_to_response('photoalbum/photo_edit.html', c)

