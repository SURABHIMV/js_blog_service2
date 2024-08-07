from django.contrib import admin
from . models import *
from django.utils.html import format_html
# Register your models here.

class Blog_Admin(admin.ModelAdmin):
    def image_tag2(self, obj):
        if obj.image:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
        else:
            return 'No Image'
    image_tag2.short_description = 'Image'
    list_display = ['auther_name','date','title','description','status','image_tag2']
admin.site.register(Blog,Blog_Admin)


class Service_Admin(admin.ModelAdmin):
    def image_tag1(self, obj):
        if obj.image:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
        else:
            return 'No Image'
    image_tag1.short_description = 'Image'
    list_display = ['title','description','status','image_tag1']
admin.site.register(Service,Service_Admin)