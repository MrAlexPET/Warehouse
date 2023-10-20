from django.contrib import admin
from.models import Artist, Album, Song, MusicShow, Win


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(MusicShow)
class MusicShowAdmin(admin.ModelAdmin):
    pass


@admin.register(Win)
class WinAdmin(admin.ModelAdmin):
    pass
