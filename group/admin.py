from django.contrib import admin
from group.models import Group, Membership

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('group', 'singer',  )

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Group, GroupAdmin)
admin.site.register(Membership, MembershipAdmin)