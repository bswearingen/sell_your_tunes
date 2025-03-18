from django.core.validators import validate_image_file_extension
from django.db import models
from django.core.files.storage import FileSystemStorage

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
    # TODO: Maximum dimensions and validation
    spine_art = models.ImageField(
        upload_to=art_dir, 
        blank=True, 
        validators=[validate_image_file_extension],
        storage=FileSystemStorage(allow_overwrite=True)
    )

    def __str__(self):
        return self.name
    class Meta:
        # Artists can't repeat album names
        unique_together = ["release_artist", "name"]
        ordering = ["release_artist", "-release_date"]
