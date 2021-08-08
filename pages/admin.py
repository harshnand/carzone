from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumnail(self,object):
        return format_html('<img src="{}" width="40/>'.format(object.photo.url))


    list_display = ('id','thumnail','first_name','designation','created_date')
    list_display_links = ('id','first_name',)
    thumnail.short_description ='photo'
    search_fields = ('first_name',)

admin.site.register(Team,TeamAdmin)