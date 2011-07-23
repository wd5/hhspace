# -*- coding: utf8 -*-
from datetime import datetime

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import save_instance
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, get_hexdigest
from account.models import Singer, Style
from customuser.models import CustomUser
from hhspace.group.models import Group, Membership

import re
import datetime
from utils.autocomplete import ModelAutoCompleteField

alnum_re = re.compile(r'^\w+$') # regexp. from jamesodo in #django

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required, field' }
now = datetime.datetime.now()

BIRTHDAY_YEARS = ()

for n in range(1920, now.year):
    BIRTHDAY_YEARS += ((n,n),)

MONTHS = map(lambda a: (a,a), ('Январь',"Февраль","Март","Апрель","Май","Июль","Июнь","Август","Сентябрь","Октябрь","Ноябрь","Декабрь",))
DAYS = map(lambda a: (a,a), range(1,13))
DATECREATED_YEARS = map(lambda a: (a,a), range(1950, 2012))

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


    birthday_year = forms.ChoiceField(
        widget=forms.Select(attrs={'class' : 'sel-small1'}),
        choices=BIRTHDAY_YEARS,
        label=_(u'Дата рождения'))
    birthday_month = forms.ChoiceField(
        widget=forms.Select( attrs={'class': 'sel-small1'}, ),
        choices=MONTHS ,
        label=_(u'.'))
    birthday_day = forms.ChoiceField(
        widget=forms.Select( attrs={'class': 'sel-small1'}, ),
        choices=DAYS ,
        label=_(u'.'))
    """
    
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_(u'Емайл'))

    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_(u'Имя'))
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,
                                                               maxlength=75)),
                             label=_(u'Фамилия'))


    birthday = forms.DateField(widget=SelectDateWidget(attrs={'class' : 'sel-small'},), label=_(u'Дата рождения'))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'Пароль'))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
                                label=_(u'Подтвеждение'))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'sex', 'birthday', 'country',  'region', 'city',  'email',   'password1',  'password2', )
        # exclude = ('biography', 'is_staff', 'password', 'is_superuser', 'status', 'mood', 'is_active', 'last_login', 'date_joined', 'groups', 'user_permissions')

    def clean_email(self):
        """
        FIXME
        Validate that the username is alphanumeric and is not already
        in use.

        """
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        
        raise forms.ValidationError(_(u'Данный емайл уже занят. Укажите другой емайл адрес либо воспользуйтесь функцией восстановления пароля'))

    def clean(self):
        """
        FIXME
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        ToDo
        """
        #self.cleaned_data['birthday'] =  "%s.%s.%s"% (self.cleaned_data['birthday_year'],self.cleaned_data['birthday_month'],self.cleaned_data['birthday_day'])
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_(u'You must type the same password each time'))
        return self.cleaned_data

    def save(self, user):
        obj = super(RegistrationForm, self).save(commit=False)
        import random
        algo = 'sha1'
        salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
        hsh = get_hexdigest(algo, salt, self.cleaned_data['password1'])
        obj.password = '%s$%s$%s' % (algo, salt, hsh)
        self.cleaned_data['password'] = obj.password
        
        if self.instance.pk is None:
            fail_message = 'created'
        else:
            fail_message = 'changed'

        return save_instance(self, self.instance, self._meta.fields,
                             fail_message, commit=True, construct=False)

class SingerRegistrationForm(RegistrationForm):

    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=attrs_dict),
                               label=_(u'Творческий псевдоним'))
    styles = ModelAutoCompleteField(lookup_url = '/style/ajax_list/',
                                    model = Style, required=False)

    directions = forms.CharField(widget=forms.HiddenInput())
    date_created = forms.DateField(widget=SelectDateWidget(attrs={'class' : 'sel-small'},), label=_(u'Дата начала деятельности'))
    reg_group = forms.ChoiceField(widget=forms.Select(), choices=((0, 'Исполнитель'), (1, 'Группа')), label = 'Регистрируюсь как ?')

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

    class Meta:
        model = Singer
        fields = ( 'reg_group', 'username', 'date_created', 'styles', 'first_name', 'last_name', 'sex', 'birthday', 'country',  'region', 'city',  'email',   'password1',  'password2', 'directions')


    def save(self, user):
        # self.directions = [ self.direction, ]
        r = super(SingerRegistrationForm, self).save(user = user)
        user.date_created = "%s %s %s" % (self.data['date_created_year'], self.data['date_created_month'], self.data['date_created_day'])
        user.birthday = "%s %s %s" % (self.data['birthday_year'], self.data['birthday_month'], self.data['birthday_day'])
        user.directions = self.data['directions']
        # r.save_m2m()
        return r

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
        exclude = ('singers', 'leaders', 'last_login', 'date_joined', 'status', 'mood', 'featuring', 'directions')


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

    def save(self, singer):
        obj = super(GroupRegistrationForm, self).save(commit=False)
        obj.date_created = datetime.datetime.now()
        obj.date_joined = datetime.datetime.now()
        r = obj.save()
        m1 = Membership(singer=singer, group=obj, date_joined = datetime.datetime.now(), invite_reason = "")
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
