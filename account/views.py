# -*- coding: utf8 -*-
import django
from django.contrib.auth import logout, authenticate
from django.core.context_processors import csrf
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.generic.simple import direct_to_template
from account.forms import BiographyForm
from account.models import CustomUser, Direction, Style, BookmarkUser
from content.models import News
from group.models import BookmarkGroup
from hhspace.account.models import Singer
from registration.forms import UserLoginForm
from hhspace.account.models import PhotoAlbum
from utils.views import edit_url

def account(request, id):

    c = {}
    c['home_tab'] = 'active'
    c['photo'] = {}

    try:
        profile = Singer.objects.get(pk=id)
        html = 'account/account_home.html'
        try:
            c['albums'] = PhotoAlbum.objects.filter(singer=profile).order_by('-date_updated')[:2]
        except PhotoAlbum.DoesNotExist:
            c['photoadd'] = 'добавить фото'
    except Singer.DoesNotExist:
        profile = CustomUser.objects.get(pk=id)
        html = 'user/user_home.html'

    c['profile'] = profile
    c['nnation_tab'] = 'active'
    c['user'] = request.user
    c['photoaddurl'] = edit_url(request.user, c['profile'], 'photoalbum_add', [c['profile'].pk] )
    c['videoaddurl'] = edit_url(request.user, c['profile'], 'video_add', [c['profile'].pk] )
    c['singers'] = Singer.objects.filter(directions__pk=c['profile'].directions.all()[0].pk).exclude(pk=profile.pk)[:10]

    return render_to_response(html, c )

def object_edit(request):

    try:
        profile = Singer.objects.get(pk=request.user.id)
        from account.forms import ProfileForm
    except Singer.DoesNotExist:
        profile = get_object_or_404(CustomUser, pk=request.user.id)
        from account.forms import UserProfileForm as ProfileForm
        
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



def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    context = { 'form': form, }
    context['nnation_tab'] = 'active'
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('/account/%d'% user.id)
        else:
            return redirect('/account/login/')
    return direct_to_template(request, 'login/form.html', context)

def logout_view(request):
    logout(request)
    return redirect('/account/login/')

def biography_view(request, singer_id):
    try:
        profile = Singer.objects.get(pk=singer_id)
    except Singer.DoesNotExist:
        profile = get_object_or_404(CustomUser, pk=singer_id)
        
    biography_tab = 'active'
    user = request.user
    profile.__class__.__name__ = 'singer'
    editurl = edit_url(user, profile, "biography_edit", [singer_id])
    nnation_tab = 'active'

    return direct_to_template(request,'account/biography.html', locals())

def biography_edit(request, singer_id):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user

    try:
        c['profile'] = Singer.objects.get(pk=request.user.id)
    except Singer.DoesNotExist:
        c['profile'] = get_object_or_404(CustomUser, pk=request.user.id)

    c['profile'].__class__.__name__ = 'singer'
    c['biography_tab'] = 'active'
    c['formurl'] = edit_url(c['user'], c['profile'], 'biography_edit', [c['profile'].pk], 0)
    c['nnation_tab'] = 'active'

    if not request.POST:
        c['profile'].biography = c['profile'].biography.replace('<br />','\n')
        form = BiographyForm(instance=c['profile'])
        c['form'] = form
        return render_to_response('account/biography_edit.html', c)
    else:
        form = BiographyForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('singer_biography_view', args=[request.user.id]))
        else:
            form = BiographyForm(request.POST)
            c['form'] = form
            return render_to_response('account/biography_edit.html', c)


def main(request):

    directions = Direction.objects.all()

    c = {}
    c.update(csrf(request))
    c['directions'] = directions
    c['user'] = request.user
    c['main_tab'] = 'active'
    try:
        c['news'] = News.objects.filter().order_by('-date_created')[:1][0]
    except News.DoesNotExist:
        c['news'] = ''

    return render_to_response('index.html', c)

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


def bookmark_add(request, id):

    if request.user.is_anonymous():
        return HttpResponse('Вам необходимо  <a href="/registration/">зарегистрироватся</a>')
    else:
        o = BookmarkUser.objects.filter(Q(user__id=request.user.id)&Q(mark__id=id)).count()
        if o == 0:
            b = BookmarkUser()
            b.user_id = request.user.id
            b.mark_id = id
            b.save()
        return HttpResponse('Добавленно')

def bookmark_list(request, id):

    users = BookmarkUser.objects.filter(user__id=request.user.id)
    groups = BookmarkGroup.objects.filter(user__id=request.user.id)

    try:
        profile = Singer.objects.get(pk=request.user.id)
    except Singer.DoesNotExist:
        profile = get_object_or_404(CustomUser, pk=request.user.id)

    user = profile

    return render_to_response('bookmark/list.html', locals() )

def bookmark_remove(request, id):

    o = BookmarkUser.objects.filter(Q(user__id=request.user.id)&Q(mark__id=id))[0].delete()
    return HttpResponse('Удалено')

def ajax_change(request, user_id):

    user = CustomUser.objects.get(pk=user_id)
    user.__setattr__(request.GET['name'],request.GET['value']);
    user.save()
    return HttpResponse(request.GET['value'])
