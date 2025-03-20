from django.core.validators import validate_image_file_extension
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .artist import Artist
class Album(models.Model):
    """
    Stores any collection of tracks: an LP, EP, single, etc.
    """
    name = models.CharField()
    description = models.TextField(blank=True)
    release_date = models.DateField()
    release_artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    contributing_artists = models.ManyToManyField(Artist, related_name='contributing_albums', blank=True)
    
    # Art
    def art_dir(self, filename):
        return '/'.join([self.release_artist.name, self.name, 'images', filename])
    # TODO: Maximum dimensions and validation
    album_cover = models.ImageField(
        upload_to=art_dir, blank=True, 
        validators=[validate_image_file_extension],
        storage=FileSystemStorage(allow_overwrite=True)
    )
    album_cover_alt_text = models.TextField(blank=True)
    # TODO: Maximum dimensions and validation
    spine_art = models.ImageField(
        upload_to=art_dir, 
        blank=True, 
        validators=[validate_image_file_extension],
        storage=FileSystemStorage(allow_overwrite=True)
    )
    spine_art_alt_text = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def activitypub(self, top_level=True):
        obj = {
            "id": '/'.join([settings.HOST, "albums", str(self.pk), '']),
            "type": "OrderedCollection",
            "name": self.name,
            "published": self.release_date,
            "generator": self.release_artist.activitypub(top_level=False),
        }

        attributed_to = []
        for member in self.contributing_artists.all():
            attributed_to.append(member.activitypub(top_level=False))
        obj["attributedTo"] = attributed_to

        obj["totalItems"] = self.track_set.count()
        
        ordered_items = []
        for track in self.track_set.all():
            ordered_items.append(
                track.activitypub(top_level=False)
            )
        obj["orderedItems"] = ordered_items
        
        if self.description:
            obj["summary"] = self.description

        if self.album_cover:
            album_cover = {
                "type": "Image",
                "url": settings.HOST + self.album_cover.url
            }
            if self.album_cover_alt_text:
                album_cover["altText"] = self.album_cover_alt_text
            obj["icon"] = album_cover
        
        if self.spine_art:
            spine_art = {
                "type": "Image",
                "url": settings.HOST + self.spine_art.url
            }
            if self.spine_art_alt_text:
                spine_art["altText"] = self.spine_art_alt_text
            obj["image"] = spine_art
        
        if top_level:
            obj["@context"] = "https://www.w3.org/ns/activitystreams"
        return obj
    class Meta:
        # Artists can't repeat album names
        unique_together = ["release_artist", "name"]
        ordering = ["release_artist", "-release_date"]
