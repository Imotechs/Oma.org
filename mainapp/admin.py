from django.contrib import admin
from .models import Artist,Genre,Song,Album,ArtistSong,Event,NewRelease,ShowSongs

# Register your models here.
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(ArtistSong)
admin.site.register(Event)
admin.site.register(NewRelease)
admin.site.register(ShowSongs)
