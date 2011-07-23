# -*- coding: utf8 -*-
import django
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth import login
from django.core.urlresolvers import reverse
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template
from account.models import Direction, Style
from content.models import News
from customuser.models import CustomUser, Region, BookmarkUser
from group.models import BookmarkGroup
from hhspace.account.models import Singer
from registration.forms import UserLoginForm
from customuser.forms import BiographyForm, UserProfileForm
from utils.views import edit_url

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

def user(request, id):

    c = {}
    c['home_tab'] = 'active'
    c['photo'] = {}

    profile = get_object_or_404(CustomUser, pk=id)
    html = 'customuser/user_home.html'

    c['profile'] = profile
    c['nnation_tab'] = 'active'
    c['user'] = request.user

    return render_to_response(html, c )

@login_required(login_url='/user/login/')
def object_edit(request):

    profile = get_object_or_404(CustomUser, pk=request.user.id)

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    c['profile'] = profile
    c['biography_tab'] = 'active'
    c['nnation_tab'] = 'active'

    if not request.POST:
        c['form'] = UserProfileForm( instance=profile)
        return render_to_response('customuser/edit.html', c)
    else:
        form = UserProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user', args=[request.user.id]))
        else:
            c['form'] = UserProfileForm(data=request.POST)
            return render_to_response('customuser/edit.html', c)


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
            try:
                Singer.objects.get(pk=user.id)
                return redirect('/account/%d'% user.id)
            except Singer.DoesNotExist:
                return redirect('/user/%d'% user.id)

        else:
            return redirect('/user/login/')
<<<<<<< HEAD
=======
        
>>>>>>> cdb9af116de101b1e108300e7cecbdcda21d1a1e
    return direct_to_template(request, 'login/form.html', context)

def logout_view(request):
    logout(request)
    return redirect('/user/login/')

def biography_view(request, user_id):

    profile = get_object_or_404(CustomUser, pk=user_id)
    biography_tab = 'active'
    user = request.user
    editurl = edit_url(user, profile, "biography_edit", [user_id])
    nnation_tab = 'active'

    return direct_to_template(request,'customuser/biography.html', locals(), RequestContext(request))

@login_required(login_url='/user/login/')
def biography_edit(request, user_id):

    csrf(request)
    user = request.user

    profile = get_object_or_404(CustomUser, pk=user_id)

    biography_tab = 'active'
    formurl = edit_url(user, profile, 'biography_edit', [profile.pk], 0)
    nnation_tab = 'active'

    if not request.POST:
        profile.biography = profile.biography.replace('<br />','\n')
        form = BiographyForm(instance=profile)
        return render_to_response('customuser/biography_edit.html', locals(), RequestContext(request))
    else:
        form = BiographyForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customuser_biography_view', args=[request.user.id]))
        else:
            form = BiographyForm(request.POST)
            return render_to_response('customuser/biography_edit.html', locals(), RequestContext(request))

def user_list(request, param, value):

    user = request.user
    nnation_tab = 'active'
    users = Singer.objects.all()
    return render_to_response('cutomuser/list.html', locals())

def ajax_user_list(request):

    limit = request.GET.get('limit', 10)
    query = request.GET.get('q', None)
    name = request.GET.get('name', 'user')
    # it is up to you how query looks
    if query:
        qargs = [django.db.models.Q(username__istartswith=query)]

    instances = CustomUser.objects.filter(django.db.models.Q(*qargs))[:limit]

    results = "[ "
    for idx, item in enumerate(instances):
        results += "{ 'id' : '%s', 'name' : '%s', 'value' : '%s' } " %(item.pk, name, item.username)
        if idx + 1 != len(instances):
            results += ", \n"

    results += " ]"

    return HttpResponse(results)

@login_required(login_url='/user/login/')
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

@login_required(login_url='/user/login/')
def bookmark_remove(request, id):

    o = BookmarkUser.objects.filter(Q(user__id=request.user.id)&Q(mark__id=id))[0].delete()
    return HttpResponse('Удалено')

@login_required(login_url='/user/login/')
def ajax_change(request, user_id):

    user = CustomUser.objects.get(pk=user_id)
    user.__setattr__(request.GET['name'],request.GET['value']);
    user.save()
    return HttpResponse(request.GET['value'])
