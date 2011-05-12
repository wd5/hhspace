# Create your views here.
from django.contrib.auth import logout
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.views.generic.simple import direct_to_template
from account.forms import BiographyForm
from hhspace.account.models import Singer
from registration.forms import UserLoginForm

def account(request):
    singer = Singer.objects.get(id=request.user.id)
    return render_to_response('account/account_home.html', { 'singer': singer })


def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    context = { 'form': form, }
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

def biography_view(request):
    return direct_to_template(request,'account/biography.html', {'user' : request.user})

def biography_edit(request):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user

    if not request.POST:
        form = BiographyForm()
        c['form'] = form
        return render_to_response('account/biography_edit.html', c)
    else:
        form = BiographyForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/biography/')
        else:
            form = BiographyForm(request.POST)
            c['form'] = form
            return render_to_response('account/biography_edit.html', c)
