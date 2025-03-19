from django.conf import settings
from django.core.validators import validate_image_file_extension
from django.db import models
from django.core.files.storage import FileSystemStorage
from .utils import user_to_activitypub

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
    profile_alt_text = models.TextField(blank=True)
    # TODO: Maximum dimensions and validation
    banner = models.ImageField(
        blank=True,
        storage=FileSystemStorage(allow_overwrite=True),
        upload_to=art_dir, 
        validators=[validate_image_file_extension],
    )
    banner_alt_text = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def activitypub(self, top_level=True):
        obj = {
            "id": '/'.join([settings.HOST, "artists", str(self.pk), '']),
            "type": "Group",
            "name": self.name,
        }

        if self.bio:
            obj["summary"] = self.bio

        if self.profile:
            profile = {
                "type": "Image",
                "url": settings.HOST + self.profile.url
            }
            if self.profile_alt_text:
                profile["altText"] = self.profile_alt_text
            obj["icon"] = profile

        if self.banner:
            banner = {
                "type": "Image",
                "url": settings.HOST + self.banner.url
            }
            if self.banner_alt_text:
                banner["altText"] = self.banner_alt_text
            obj["image"] = banner
            
        if self.origin:
            obj["location"] = {
                "name": self.origin,
                "type": "Place"
            }
        
        members = []
        for member in self.members.all():
            members.append(user_to_activitypub(member, top_level=False))
        obj["attributedTo"] = members

        if top_level:
            obj["@context"] = "https://www.w3.org/ns/activitystreams"
        
        return obj