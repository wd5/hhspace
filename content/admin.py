from content.models import News, Page, Event
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', )

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', )

class PageAdmin(admin.ModelAdmin):
    list_display = ('title',  )

admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)
  