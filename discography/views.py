from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from account.models import Singer
from discography.forms import SingerAlbumForm, SingerTrackForm
from discography.models import SingerAlbum, TrackSingerAblum


def albumcollection_view(request):
    singer = Singer.objects.get(customuser_ptr=request.user.id)
    
    try:
        albums = SingerAlbum.objects.filter(singer=singer)
    except SingerAlbum.DoesNotExist:
        albums = {}
        
    return direct_to_template(request, 'discography/albumcollection.html', { 'albums' : albums } )

def album_view(request, id):

    try:
        tracks = TrackSingerAblum.objects.filter(album=id)
    except SingerAlbum.DoesNotExist:
        tracks = {}

    return direct_to_template(request,'discography/album.html', { 'album' : SingerAlbum.objects.get(pk=id), 'tracks' : tracks})

def album_edit(request):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user

    if not request.POST:
        form = SingerAlbumForm()
        c['form'] = form
        return render_to_response('discography/album_edit.html', c)
    else:
        form = SingerAlbumForm(request.POST,  request.FILES)
        if form.is_valid():
            album = form.save(request.user.id)
            return HttpResponseRedirect('/discography/album/{0:d}/'.format(album.pk))
        else:
            form = SingerAlbumForm(request.POST, request.FILES)
            c['form'] = form
            return render_to_response('discography/album_edit.html', c)

def track_edit(request, album_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    album = SingerAlbum.objects.get(pk=album_id)
    c['album'] = album

    if not request.POST:
        form = SingerTrackForm()
        c['form'] = form
        return render_to_response('discography/track_edit.html', c)
    else:
        form = SingerTrackForm(request.POST)
        if form.is_valid():
            track = form.save(album_id)
            return HttpResponseRedirect('/discography/album/{0:d}/'.format(album.pk))
        else:
            form = SingerTrackForm(request.POST)
            c['form'] = form
            return render_to_response('discography/track_edit.html', c)
