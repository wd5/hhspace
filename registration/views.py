from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf

from hhspace.account.models import Direction
from hhspace.account.models import Region
from hhspace.account.models import City
from hhspace.account.models import Country
from hhspace.account.forms import RegistrationForm
from django.views.generic.simple import direct_to_template
from account.forms import UserLoginForm, RegistrationFormTermsOfService
from django.contrib.auth import logout
from django.contrib import auth
from account.models import CustomUser


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
                    return HttpResponseRedirect('/registration/complete/')
                else:
                    form = RegistrationForm(request.POST)
                    c['form'] = form
                    return render_to_response('registration/step3_user.html', c)
    else:
        form = RegistrationFormTermsOfService(request.POST or None)
        c['form'] = form
        
        if request.method == 'POST' and form.is_valid():
            directions = Direction.objects.all()
            return render_to_response('registration/step2.html', c)

        return render_to_response('registration/step1.html', c)

def user_login_view(request):
    form = UserLoginForm(request.POST or None)
    context = { 'form': form, }
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/account/login/')
    return direct_to_template(request, 'login/form.html', context)

def logout_view(request):
    logout(request)
    return redirect('/account/login/')
    # Redirect to a success page.
