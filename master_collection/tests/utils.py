from django.conf import settings
from django.contrib.auth.models import User
from master_collection.models import Artist, Album, Track
from django.core.files.uploadedfile import SimpleUploadedFile

BASE_URL = settings.HOST

"""
-----------------------------------------------------
|                                                   |
|                                                   |
|        Functions for creating test data           |
|                                                   |
|                                                   |
-----------------------------------------------------
"""
def create_users(usernames):
    users = []
    for username in usernames:
        users.append(User.objects.create_user(username=username, password='12345'))

    return users

def create_artists(artist_names, users):
    artists = []
    for artist_name in artist_names:
        artist = Artist.objects.create(name=artist_name)
        artist.members.set([users.pop(0), users.pop(0)])
        artists.append(artist)

    return artists

def create_albums(artist, album_names):
    albums = []
    for album_name in album_names:
        album = Album.objects.create(
            name=album_name,
            release_date="1990-01-01",
            release_artist=artist,
        )
        albums.append(album)
    
    return albums

def create_tracks(album, track_names):
    i = 1
    for track_name in track_names:
        Track.objects.create(
            name=track_name,
            order=i,
            album=album,
            master_recording=SimpleUploadedFile("its_a_real_song.flac",b"these are the file contents!")
        )
        i += 1


"""
-----------------------------------------------------
|                                                   |
|                                                   |
|        Expected Messages                          |
|                                                   |
|                                                   |
-----------------------------------------------------
"""

expected_get_albums_response = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "summary": "sell_your_tune's master album collection",
    "type": "OrderedCollection",
    "totalItems": 5,
    "orderedItems": [
        {
            "summary": "One Time created an album: 1st Album",
            "type": "Create",
            "attributedTo": BASE_URL + "artists/2/",
            "actor": {
                "type": "Group",
                "name": "One Time",
                "id": BASE_URL + "artists/2/",
            },
            "object": {
                "type": "Audio",
                "name": "1st Album",
                "id": BASE_URL + "albums/1/",
                "published": "1990-01-01",
            }
        },
        {
            "summary": "Multipack created an album: 2nd Album",
            "type": "Create",
            "attributedTo": BASE_URL + "artists/3/",
            "actor": {
                "type": "Group",
                "name": "Multipack",
                "id": BASE_URL + "artists/3/",
            },
            "object": {
                "type": "Audio",
                "name": "2nd Album",
                "id": BASE_URL + "albums/2/",
                "published": "1990-01-01",
            }
        },
        {
            "summary": "Multipack created an album: 3rd Album",
            "type": "Create",
            "attributedTo": BASE_URL + "artists/3/",
            "actor": {
                "type": "Group",
                "name": "Multipack",
                "id": BASE_URL + "artists/3/",
            },
            "object": {
                "type": "Audio",
                "name": "3rd Album",
                "id": BASE_URL + "albums/3/",
                "published": "1990-01-01",
            }
        },
        {
            "summary": "Multipack created an album: 4th Album",
            "type": "Create",
            "attributedTo": BASE_URL + "artists/3/",
            "actor": {
                "type": "Group",
                "name": "Multipack",
                "id": BASE_URL + "artists/3/",
            },
            "object": {
                "type": "Audio",
                "name": "4th Album",
                "id": BASE_URL + "albums/4/",
                "published": "1990-01-01",
            }
        },
        {
            "summary": "Multipack created an album: 5th Album",
            "type": "Create",
            "attributedTo": BASE_URL + "artists/3/",
            "actor": {
                "type": "Group",
                "name": "Multipack",
                "id": BASE_URL + "artists/3/",
            },
            "object": {
                "type": "Audio",
                "name": "5th Album",
                "id": BASE_URL + "albums/5/",
                "published": "1990-01-01",
            }
        },
    ]
} 

expected_get_artists_response = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "summary": "sell_your_tune's master artist collection",
    "type": "OrderedCollection",
    "totalItems": 3,
    "orderedItems": [
        {
            "summary": "NoAlbum1 created a new band: No Album",
            "type": "Create",
            "attributedTo": BASE_URL + "1/",
            "actor": {
                "type": "Person",
                "name": "NoAlbum1",
                "id": BASE_URL + "1/",
            },
            "object": {
                "type": "Group",
                "name": "No Album",
                "id": BASE_URL + "artists/1/",
            }
        },
        {
            "summary": "OneTime1 created a new band: One Time",
            "type": "Create",
            "attributedTo": BASE_URL + "3/",
            "actor": {
                "type": "Person",
                "name": "OneTime1",
                "id": BASE_URL + "3/",
            },
            "object": {
                "type": "Group",
                "name": "One Time",
                "id": BASE_URL + "artists/2/",
            }
        },
        {
            "summary": "Multipack1 created a new band: Multipack",
            "type": "Create",
            "attributedTo": BASE_URL + "5/",
            "actor": {
                "type": "Person",
                "name": "Multipack1",
                "id": BASE_URL + "5/",
            },
            "object": {
                "type": "Group",
                "name": "Multipack",
                "id": BASE_URL + "artists/3/",
            }
        },
    ]
} 

expected_get_album_response = {
    "summary": "One Time created an album: 1st Album",
    "type": "Create",
    "attributedTo": BASE_URL + "artists/2/",
    "actor": {
        "type": "Group",
        "name": "One Time",
        "id": BASE_URL + "artists/2/",
    },
    "object": {
        "type": "Audio",
        "name": "1st Album",
        "id": BASE_URL + "albums/1/",
        "published": "1990-01-01",
        "attachment":[
            # TODO: Include tracks here
        ]
    }
}

expected_get_artist_response = {
    "summary": "NoAlbum1 created a new band: No Album",
    "type": "Create",
    "attributedTo": BASE_URL + "1/",
    "actor": {
        "type": "Person",
        "name": "NoAlbum1",
        "id": BASE_URL + "1/",
    },
    "object": {
        "type": "Group",
        "name": "No Album",
        "id": BASE_URL + "artists/1/",
    }
}