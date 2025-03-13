from django.contrib import admin

from .models import Artist, Album, Track

class TrackInline(admin.StackedInline):
    model = Track
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "members"]}),
        ("Description", {"fields": ["origin", "bio"]}),
        ("Art", {"fields": ["profile", "banner"]})
    ]

class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)