from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth import login, authenticate
from account.models import Singer

from hhspace.account.models import Direction
from hhspace.registration.forms import RegistrationForm
from django.views.generic.simple import direct_to_template
from registration.forms import UserLoginForm, RegistrationFormTermsOfService, SingerRegistrationForm, GroupRegistrationForm


def register(request):
    step = int(request.POST.get('step', 1))
    role = request.GET.get('role', 0)
    c = {}
    c.update(csrf(request))
    c['user'] = request.user

    if role != 0:
        if role == 'user':
            if not request.POST:
                form = RegistrationForm()
                c['form'] = form
                return render_to_response('registration/step3_user.html', c)
            else:
                form = RegistrationForm(data=request.POST)
                if form.is_valid():
                    form.save(request.user)

                    user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
                    if user and user.is_active:
                        login(request, user)

                    return HttpResponseRedirect('/registration/complete/')
                else:
                    form = RegistrationForm(request.POST)
                    c['form'] = form
                    return render_to_response('registration/step3_user.html', c)
        else:
            if not request.POST:
                form = SingerRegistrationForm(initial={ 'directions' : request.GET.get('role', 0) })
                c['form'] = form
                return render_to_response('registration/step3_singer.html', c)
            else:
                form = SingerRegistrationForm(data=request.POST)
                if form.is_valid():
                    form.save(request.user)
                    
                    user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
                    if user and user.is_active:
                        login(request, user)

                    gr = request.POST.get('reg_group', 0)
                    if gr != '0':
                        return HttpResponseRedirect(reverse('group_edit'))
                    else:
                        return HttpResponseRedirect(reverse('account', args=[user.pk]))
                else:
                    form = SingerRegistrationForm(request.POST)
                    c['form'] = form
                    return render_to_response('registration/step3_singer.html', c)

    else:
        form = RegistrationFormTermsOfService(request.POST or None)
        c['form'] = form
        
        if request.method == 'POST' and form.is_valid():
            directions = Direction.objects.all()
            c['directions'] = directions
            return render_to_response('registration/step2.html', c)

        return render_to_response('registration/step1.html', c)

def register_group(request):

    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    import logging

    sviewlog = logging.getLogger('account.views')
    view_log_handler = logging.FileHandler('/tmp/scan_log.log')
    view_log_handler.setLevel(logging.INFO)
    view_log_handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
    sviewlog.addHandler(view_log_handler)
    
    if not request.POST:
        form = GroupRegistrationForm()
        c['form'] = form
        return render_to_response('registration/group.html', c)
    else:
        form = GroupRegistrationForm(data=request.POST)
        if form.is_valid():
            sviewlog.error(request.user.id)
            singer = Singer.objects.get(id=request.user.id)
            form.save(singer)
            return HttpResponseRedirect('/registration/group/complete/')
        else:
            form = GroupRegistrationForm(request.POST)
            c['form'] = form
            return render_to_response('registration/group.html', c)


