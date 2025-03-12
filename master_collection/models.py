from django.conf import settings
from django.core.validators import FileExtensionValidator, validate_image_file_extension 
from django.db import models

class Artist(models.Model):
    """
    Stores a musical creator: an individual artist, a band, an ensemble, etc.
    Creates :model:`master_collection.Album` and :model:`master_collection.Recording`.
    """
    name = models.CharField(unique=True)
    bio = models.TextField(blank=True)
    origin = models.CharField("origin city", blank=True)
    # Members tie back to actual user accounts on the server
    # TODO: Adding anyone should generate an invitation to associate yourself with the Artist
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    # Art
    def art_dir(self, filename):
        return '/'.join([self.name, 'images', filename])
    # TODO: Maximum dimensions and validation
    profile = models.ImageField(upload_to=art_dir, blank=True)
    # TODO: Maximum dimensions and validation
    banner = models.ImageField(upload_to=art_dir, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    """
    Stores any collection of recordings: an LP, EP, single, etc.
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
    album_cover = models.ImageField(upload_to=art_dir, blank=True, validators=[validate_image_file_extension])
    # TODO: Maximum dimensions and validation
    spine_art = models.ImageField(upload_to=art_dir, blank=True, validators=[validate_image_file_extension])

    def __str__(self):
        return self.name
    class Meta:
        # Artists can't repeat album names
        unique_together = ["release_artist", "name"]
        ordering = ["release_artist", "-release_date"]

class Track(models.Model):
    """
    Stores a represenation of a single song or recording. Multiple file types and qualities can be
    represented with :model:`master_collection.RecordingFile`.
    """
    name = models.CharField()
    order = models.IntegerField()
    lyrics = models.TextField(blank=True)
    # Each recording is associated with one album.
    # If people want to include the same song in multiple albums, at this point
    # they'll need to re-upload. If this becomes a problem, change this to ManyToManyField
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        # Each track has a spot in the album order
        unique_together = ["album", "order"]
        ordering = ["order"]


# TODO: Limit the number of recording files per recording.
class Recording(models.Model):
    """
    Stores an individual file for a recording. This allows varying filetypes and qualities.
    """
    def upload_dir(self, filename):
        return '/'.join([self.track.album.release_artist.name, self.track.album.name, self.track.name, filename])

    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    # TODO: Determine desired filetypes.
    # TODO: Maximum size.
    file = models.FileField(
        upload_to=upload_dir,
        validators=[FileExtensionValidator(allowed_extensions=["mp3"])]
    )
    for_streaming = models.BooleanField(default=False)
