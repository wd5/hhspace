# -*- coding: utf8 -*-
import django
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template
from account.models import PhotoAlbum, Style
from customuser.forms import BiographyForm
from customuser.models import CustomUser
from hhspace.account.models import Singer
from registration.forms import UserLoginForm
from utils.views import edit_url

def account(request, id):

    c = {}
    c['home_tab'] = 'active'
    c['photo'] = {}

    profile = Singer.objects.get(pk=id)
    html = 'account/account_home.html'
    try:
        c['albums'] = PhotoAlbum.objects.filter(singer=profile).order_by('-date_updated')[:2]
    except PhotoAlbum.DoesNotExist:
        c['photoadd'] = 'добавить фото'

    c['profile'] = profile
    c['nnation_tab'] = 'active'
    c['user'] = request.user
    c['photoaddurl'] = edit_url(request.user, c['profile'], 'photoalbum_add', [c['profile'].pk] )
    c['videoaddurl'] = edit_url(request.user, c['profile'], 'video_add', [c['profile'].pk] )
    c['singers'] = Singer.objects.filter(directions__pk=c['profile'].directions.all()[0].pk).exclude(pk=profile.pk)[:10]

    return render_to_response(html, c )


def object_edit(request):

    profile = Singer.objects.get(pk=request.user.id)
    from account.forms import ProfileForm

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = profile
    c['biography_tab'] = 'active'
    c['nnation_tab'] = 'active'

    if not request.POST:
        c['form'] = ProfileForm(instance=profile)
        return render_to_response('account/profile_edit.html', c)
    else:
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account', args=[request.user.id]))
        else:
            c['form'] = ProfileForm(data=request.POST)
            return render_to_response('account/profile_edit.html', c)


def biography_view(request, singer_id):

    profile = get_object_or_404(Singer, pk=singer_id)
    biography_tab = 'active'
    user = request.user
    editurl = edit_url(user, profile, "biography_edit", [singer_id,])
    nnation_tab = 'active'

    return direct_to_template(request,'customuser/biography.html', locals(), RequestContext(request))

def biography_edit(request, singer_id):

    update(csrf(request))
    user = request.user

    profile = get_object_or_404(Singer, pk=singer_id)

    biography_tab = 'active'
    formurl = edit_url(user, profile, 'biography_edit', [profile.pk, 0])
    nnation_tab = 'active'

    if not request.POST:
        profile.biography = profile.biography.replace('<br />','\n')
        form = BiographyForm(instance=profile)
        return render_to_response('customuser/biography_edit.html', locals(), RequestContext(request))
    else:
        form = BiographyForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('singer_biography_view', args=[request.user.id]))
        else:
            form = BiographyForm(request.POST)
            return render_to_response('customuser/biography_edit.html', locals(), RequestContext(request))
        
def account_list(request, param, value):

    user = request.user
    nnation_tab = 'active'
    singers = Singer.objects.filter(directions__id=value)
    return render_to_response('account/singer_list.html', locals())

def ajax_singer_list(request):

    limit = request.GET.get('limit', 10)
    query = request.GET.get('q', None)
    name = request.GET.get('name', 'singers')
    # it is up to you how query looks
    if query:
        qargs = [django.db.models.Q(username__istartswith=query)]

    instances = Singer.objects.filter(django.db.models.Q(*qargs))[:limit]

    results = "[ "
    for idx, item in enumerate(instances):
        results += "{ 'id' : '%s', 'name' : '%s', 'value' : '%s' } " %(item.pk, name, item.username)
        if idx + 1 != len(instances):
            results += ", \n"

    results += " ]"

    return HttpResponse(results)

def ajax_style_list(request):

    limit = request.GET.get('limit', 20)
    query = request.GET.get('q', None)
    name = request.GET.get('name', 'styles')
    # it is up to you how query looks
    if query:
        qargs = [django.db.models.Q(name__istartswith=query)]

    instances = Style.objects.filter(django.db.models.Q(*qargs))[:limit]

    results = "[ "
    for idx, item in enumerate(instances):
        results += "{ 'id' : '%s', 'name' : '%s', 'value' : '%s' } " %(item.pk, name, item.name)
        if idx + 1 != len(instances):
            results += ", \n"

    results += " ]"

    return HttpResponse(results)
