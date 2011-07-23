from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template
from hhspace.account.models import Singer, SingerAlbum, TrackSingerAblum
from hhspace.account.forms import SingerAlbumForm, SingerTrackForm
from utils.views import edit_url

def discography_list(request, singer_id):
    profile = Singer.objects.get(customuser_ptr=singer_id)

    try:
        albums = SingerAlbum.objects.filter(singer=profile)
    except SingerAlbum.DoesNotExist:
        albums = {}

    disco_tab = 'active'
    editurl = edit_url(request.user, profile, "discography_add", [request.user.id])
    nnation_tab = 'active'

    return direct_to_template(request, 'discography/album_list.html', locals() )

def discography_view(request, singer_id, album_id):

    album = get_object_or_404(SingerAlbum, pk=album_id)
    profile = get_object_or_404(Singer, pk=singer_id)
    disco_tab = 'active'
    nnation_tab = 'active'

    editurl = edit_url(request.user, profile, "track_edit", [request.user.id, album_id])

    try:
        tracks = TrackSingerAblum.objects.filter(album=album_id)
    except TrackSingerAblum.DoesNotExist:
        tracks = {}

    return direct_to_template(request, 'discography/album.html', locals() )

@login_required(login_url='/user/login/')
def album_edit(request, singer_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = Singer.objects.get(pk=singer_id)
    c['disco_tab'] = 'active'
    c['formurl']  = edit_url(request.user, c['profile'], "discography_add", [request.user.id], 0)
    c['nnation_tab'] = 'active'

    if not request.POST:
        form = SingerAlbumForm()
        c['form'] = form
        return render_to_response('discography/album_edit.html', c)
    else:
        form = SingerAlbumForm(request.POST,  request.FILES)
        if form.is_valid():
            album = form.save(request.user.id)
            return HttpResponseRedirect(reverse('singer_discography_view', args=[request.user.pk, album.pk]))
        else:
            form = SingerAlbumForm(request.POST, request.FILES)
            c['form'] = form
            return render_to_response('discography/album_edit.html', c)

@login_required(login_url='/user/login/')
def track_edit(request, album_id, singer_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile']= Singer.objects.get(pk=singer_id)
    album = SingerAlbum.objects.get(pk=album_id)
    c['album'] = album
    c['disco_tab'] = 'active'
    c['formurl']  = edit_url(request.user, c['profile'], "track_edit", [request.user.id, album_id], 0)
    c['nnation_tab'] = 'active'

    if not request.POST:
        form = SingerTrackForm(initial={ 'perform_by': c['profile'].username })
        c['form'] = form
        return render_to_response('discography/track_edit.html', c)
    else:
        form = SingerTrackForm(request.POST)
        if form.is_valid():
            track = form.save(album_id)
            return HttpResponseRedirect(reverse('singer_discography_view', args=[request.user.pk, album.pk]))
        else:
            form = SingerTrackForm(request.POST)
            c['form'] = form
            return render_to_response('discography/track_edit.html', c)
