from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from .album import Album

class Track(models.Model):
    """
    Stores a represenation of a single song or track.
    """
    name = models.CharField()
    order = models.IntegerField(validators=[MinValueValidator(1)])
    lyrics = models.TextField(blank=True)
    # Each track is associated with one album.
    # If people want to include the same song in multiple albums, at this point
    # they'll need to re-upload. If this becomes a problem, change this to ManyToManyField
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def master_upload_dir(self, filename):
        return '/'.join([self.album.release_artist.name, self.album.name, self.name + ".flac"])
    def streamable_upload_dir(self, filename):
        return '/'.join([self.album.release_artist.name, self.album.name, self.name + ".aac"])
    
    master_recording = models.FileField(
        upload_to=master_upload_dir,
        validators=[FileExtensionValidator(allowed_extensions=["flac"])],
        max_length=500,
        storage=FileSystemStorage(allow_overwrite=True)
    )
    # TODO: This should be computed in-server, rather than letting users upload this version themselves.
    streamable_recording = models.FileField(
        upload_to=streamable_upload_dir,
        validators=[FileExtensionValidator(allowed_extensions=["aac"])],
        blank=True,
        max_length=500,
        storage=FileSystemStorage(allow_overwrite=True)
    )
    def __str__(self):
        return self.name
    
    def activitypub(self, top_level=True):
        obj = {
            "id": '/'.join([settings.HOST, "tracks", str(self.pk), '']),
            "type": "Audio",
            "name": self.name,
        }
        
        if self.streamable_recording:
            obj["url"] = {
                "type": "Link",
                "href": settings.HOST + self.streamable_recording.url,
                "mediaType": "audio/aac",
            }

        if top_level:
            obj["@context"] = "https://www.w3.org/ns/activitystreams"
        
        return obj
    
    class Meta:
        # Each track has a spot in the album order
        unique_together = ["album", "order"]
        ordering = ["order"]