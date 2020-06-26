from django.contrib import admin

from .models import songs

@admin.register(songs)
class SongsAdmin(admin.ModelAdmin):
    pass
