# -*- coding: utf8 -*-
from django.utils.html import linebreaks
from django import forms
from customuser.models import CustomUser, City, Region, Country, Message
import hhspace
from utils.autocomplete import ModelAutoCompleteField

class UserProfileForm(forms.ModelForm):

    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Псевдоним')
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Имя')
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Фамилия')
    country  = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'field'}), queryset=Country.objects.all(), label=u'Страна')
    region = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'field'}), queryset=Region.objects.all(), label=u'Регион')
    city = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'field'}), queryset=City.objects.all(), label=u'Город')
    status = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Статус')
    mood = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Настроение')
    url = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Сайт', required=False)
    birthday = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'День рождения')

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',  'status', 'mood', 'url', 'birthday', )

    def save(self):
        obj = super(UserProfileForm, self).save(commit=False)
        return obj.save()


class BiographyForm(forms.ModelForm):

    biography = forms.CharField(max_length=2048, widget=forms.Textarea(attrs={'class':'field'}), label = 'Биография  ')

    class Meta:
        model = CustomUser
        fields = ('biography', )

    def save(self):
        obj = super(BiographyForm, self).save(commit=False)
        obj.biography = obj.biography.replace('\n','<br />')
        return obj.save()


class MessageForm(forms.ModelForm):

    # ffrom = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'От')
    to_id = ModelAutoCompleteField(lookup_url = '/singer/ajax_list/?name=to_id',  model = CustomUser, required=True, label = 'Кому')
    theme = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Тема')
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'field acfb-input'}), label = 'Сообщение')

    class Meta:
        model = Message
        fields = ('to_id', 'theme', 'message', )

class MessageReplyForm(forms.ModelForm):

    # ffrom = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'От')
    to_id = forms.CharField(widget=forms.HiddenInput())
    theme = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'field'}), label = 'Тема')
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'field acfb-input'}), label = 'Сообщение')

    class Meta:
        model = Message
        fields = ('to_id', 'theme', 'message', )
