from hhspace.account.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AdminPasswordChangeForm
from hhspace.account.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'image')}),
    )


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('name', )

class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', )

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', )

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )

class CustomUserAdmin(UserAdmin):
    list_display = ('username', )

class SingerAdmin(admin.ModelAdmin):
    list_display = ('username', )

admin.site.register(Direction, DirectionAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Singer, SingerAdmin)


