from django.contrib import admin

from gcalendar.models import Calendar

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('slug', 'username', 'title', 'mode')

admin.site.register(Calendar, CalendarAdmin)
