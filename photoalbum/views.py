from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from account.models import Singer
from photoalbum.forms import PhotoAlbumForm, PhotoForm
from photoalbum.models import Photo, Photoalbum


def albums_view(request):
    singer = Singer.objects.get(customuser_ptr=request.user.id)
    
    try:
        albums = Photoalbum.objects.filter(singer=singer)
    except Photoalbum.DoesNotExist:
        albums = {}

    return direct_to_template(request, 'photoalbum/albums.html', { 'albums' : albums } )

def album_view(request, id):

    try:
        photos = Photo.objects.filter(album=id)
    except Photo.DoesNotExist:
        photos = {}

    return direct_to_template(request,'photoalbum/album.html', { 'album' : Photoalbum.objects.get(pk=id), 'photos' : photos  })

def album_edit(request):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user

    if not request.POST:
        form = PhotoAlbumForm()
        c['form'] = form
        return render_to_response('photoalbum/album_edit.html', c)
    else:
        form = PhotoAlbumForm(request.POST,  request.FILES)
        if form.is_valid():
            album = form.save(request.user.id)
            return HttpResponseRedirect('/photoalbum/album/{0:d}/'.format(album.pk))
        else:
            form = PhotoAlbumForm(request.POST, request.FILES)
            c['form'] = form
            return render_to_response('photoalbum/album_edit.html', c)

def photo_edit(request, album_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    album = Photoalbum.objects.get(pk=album_id)
    c['album'] = album

    if not request.POST:
        form = PhotoForm()
        c['form'] = form
        return render_to_response('photoalbum/photo_edit.html', c)
    else:
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            track = form.save(album_id)
            return HttpResponseRedirect('/photoalbum/album/{0:d}/'.format(album.pk))
        else:
            form = PhotoForm(request.POST, request.FILES)
            c['form'] = form
            return render_to_response('photoalbum/photo_edit.html', c)
