from django.contrib import admin
from.models import Artist, Album, Win


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Win)
class WinAdmin(admin.ModelAdmin):
    pass
