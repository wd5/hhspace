from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AdminPasswordChangeForm
from customuser.models import Region, Country, City
from hhspace.customuser.models import CustomUser


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
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', )}),
    )

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', )

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)
admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)