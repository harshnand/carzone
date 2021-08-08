from django.contrib import admin
from .models import Car

# Register your models here.
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumnail(self,object):
        return format_html('<img src="{}" width="60"/>'.format(object.car_photo.url))


    list_display = ('id','thumnail', 'car_title','color','model','price','city','state','is_featured')
    list_display_links = ('id','car_title',)
    thumnail.short_description ='photo'
    search_fields = ('first_name',)
    list_editable = ('is_featured',)

admin.site.register(Car,TeamAdmin)


