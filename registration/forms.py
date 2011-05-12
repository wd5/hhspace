# -*- coding: utf8 -*-
from datetime import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, get_hexdigest
from account.models import CustomUser, Singer, Group, Membership

import re
alnum_re = re.compile(r'^\w+$') # regexp. from jamesodo in #django

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should either preserve the base ``save()`` or implement
    a ``save()`` which accepts the ``profile_callback`` keyword
    argument and passes it through to
    ``RegistrationProfile.objects.create_inactive_user()``.


    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=attrs_dict),
                               label=_(u'username'))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_(u'email address'))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'password'))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'password (again)'))
    """

    
    class Meta:
        model = CustomUser
        exclude = ('is_staff', 'is_superuser', 'status', 'mood', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions')

    def clean_username(self):
        """
        FIXME
        Validate that the username is alphanumeric and is not already
        in use.

        """
        if not alnum_re.search(self.cleaned_data['username']):
            raise forms.ValidationError(_(u'Usernames can only contain letters, numbers and underscores'))
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_(u'This username is already taken. Please choose another.'))

    def clean(self):
        """
        FIXME
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data

    def save(self, user):
        obj = super(RegistrationForm, self).save(commit=False)
        import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, self.cleaned_data['password'])
        obj.password = '%s$%s$%s' % (algo, salt, hsh)
        return obj.save()


class SingerRegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kw):
        super(SingerRegistrationForm, self).__init__(*args, **kw)
        """
        self.fields.keyOrder = [
                'username',
                'first_name',
                'last_name',
                'email',
                'password',
        ]
        """
        
    class Meta:
        model = Singer
        exclude = ('is_staff', 'is_superuser', 'status', 'mood', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions', 'featuring')


    def clean_username(self):
        if not alnum_re.search(self.cleaned_data['username']):
            raise forms.ValidationError(_(u'Usernames can only contain letters, numbers and underscores'))
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_(u'This username is already taken. Please choose another.'))

    def clean(self):
        """
        FIXME
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data

    def save(self, user):
        obj = super(SingerRegistrationForm, self).save(commit=False)
        import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, self.cleaned_data['password'])
        obj.password = '%s$%s$%s' % (algo, salt, hsh)
        return obj.save()

class GroupRegistrationForm(forms.ModelForm):

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Название')
    date_created = forms.DateField(required=False, initial="", widget=forms.DateInput(attrs={'class':'field'}), label = 'Дата создания')

    def __init__(self, *args, **kw):
        super(GroupRegistrationForm, self).__init__(*args, **kw)
        """
        self.fields.keyOrder = [
                'username',
                'first_name',
                'last_name',
                'email',
                'password',
        ]
        """

    class Meta:
        model = Group
        exclude = ('users', 'leaders', 'last_login', 'date_joined', 'status', 'mood', 'featuring')


    def clean_username(self):
        if not alnum_re.search(self.cleaned_data['name']):
            raise forms.ValidationError(_(u'name can only contain letters, numbers and underscores'))
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['name'])
        except User.DoesNotExist:
            return self.cleaned_data['name']
        raise forms.ValidationError(_(u'This name is already taken. Please choose another.'))

    def clean(self):
        """
        FIXME
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.


        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
                """
        return self.cleaned_data

    def save(self, user):
        obj = super(GroupRegistrationForm, self).save(commit=False)
        obj.date_created = datetime.now()
        obj.date_joined = datetime.now()
        r = obj.save()
        m1 = Membership(user=user, group=obj, date_joined = datetime.now(), invite_reason = "__")
        m1.save()
        return r
    
class RegistrationFormTermsOfService(forms.Form):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.

    """
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                             label=_(u'I have read and agree to the Terms of Service'))

    def clean_tos(self):
        """
        Validate that the user accepted the Terms of Service.

        """
        if self.cleaned_data.get('tos', False):
            return self.cleaned_data['tos']
        raise forms.ValidationError(_(u'You must agree to the terms to register'))

class UserLoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), max_length=30)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)
