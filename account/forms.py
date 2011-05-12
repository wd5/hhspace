# -*- coding: utf8 -*-
from account.models import CustomUser
from django import forms

class BiographyForm(forms.ModelForm):

    biography = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'class':'field'}), label = 'Биография  ')

    class Meta:
        model = CustomUser
        fields = ('biography', )

    def save(self):
        obj = super(BiographyForm, self).save(commit=False)
        return obj.save()