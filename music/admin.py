from django.contrib import admin
from music.models import Album, Songs

class Album_admin(admin.ModelAdmin):
    list_display=['Album_name']
class Songs_admin(admin.ModelAdmin):
    list_display=['Album_name','Song_name','Singer']

admin.site.register(Album, Album_admin)
admin.site.register(Songs, Songs_admin)
