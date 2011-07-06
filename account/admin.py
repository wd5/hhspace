from hhspace.account.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AdminPasswordChangeForm
from hhspace.account.models import CustomUser

class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', )

class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CustomUserAdmin(UserAdmin):
    list_display = ('username', )

class SingerAdmin(admin.ModelAdmin):
    list_display = ('username', )

admin.site.register(Direction, DirectionAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Singer, SingerAdmin)


