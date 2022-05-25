from django.contrib import admin
from .models import Music

# Register your models here.
@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'genre', 'year', 'timestamp', 'updated', 'user')
    list_filter = ('title', 'artist', 'album', 'genre', 'year', 'timestamp', 'updated', 'user')
    search_fields = ('title', 'artist', 'album', 'genre', 'year', 'timestamp', 'updated', 'user')