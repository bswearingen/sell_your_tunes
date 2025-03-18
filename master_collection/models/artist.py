from django.conf import settings
from django.core.validators import validate_image_file_extension
from django.db import models
from django.core.files.storage import FileSystemStorage

class Artist(models.Model):
    """
    Stores a musical creator: an individual artist, a band, an ensemble, etc.
    Creates :model:`master_collection.Album` and :model:`master_collection.Track`.
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
    profile = models.ImageField(
        blank=True,
        storage=FileSystemStorage(allow_overwrite=True),
        upload_to=art_dir, 
        validators=[validate_image_file_extension],
    )
    # TODO: Maximum dimensions and validation
    banner = models.ImageField(
        blank=True,
        storage=FileSystemStorage(allow_overwrite=True),
        upload_to=art_dir, 
        validators=[validate_image_file_extension],
    )

    def __str__(self):
        return self.name
    
    def activitypub(self, top_level=True):
        obj = {
            "id": '/'.join([settings.HOST, "artists", str(self.pk), '']),
            "type": "Group",
            "name": self.name,
        }

        # TODO: Implement/uncomment this
        # members = []
        # for member in self.members.all():
            # members.add({
            #     member.activitypub(top_level=False)
            # })
            
        if top_level:
            obj["@context"] = "https://www.w3.org/ns/activitystreams"
        
        return obj