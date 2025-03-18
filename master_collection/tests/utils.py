from django.conf import settings
from django.contrib.auth.models import User
from master_collection.models import Artist, Album, Track
from django.core.files.uploadedfile import SimpleUploadedFile

BASE_URL = settings.HOST

"""
-----------------------------------------------------
|                                                   |
|                                                   |
|        Expected Messages                          |
|                                                   |
|                                                   |
-----------------------------------------------------
"""
expected_get_album_1_response = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": BASE_URL + "/albums/1/",
    "type": "OrderedCollection",
    "name": "Drive",
    "summary": "Drive by Leviathan Wakes",
    "totalItems": 2,
    "attributedTo": [
        {
            "id": BASE_URL + "/artists/1/",
            "type": "Group",
            "name": "Leviathan Wakes",
        },
        {
            "id": BASE_URL + "/artists/5/",
            "type": "Group",
            "name": "Babylon's Ashes",
        },
    ],
    "orderedItems": [
        {
            "id": BASE_URL + "/tracks/3/",
            "type": "Audio",
            "name": "Symphony No. 1",
            "url": {
                "type": "Link",
                "href": BASE_URL + settings.MEDIA_URL + "Leviathan%20Wakes/Drive/Symphony%20No.%201.aac",
                "mediaType": "audio/aac"
            }
        },
        {
            "id": BASE_URL + "/tracks/4/",
            "type": "Audio",
            "name": "String Quartet",
            "url": {
                "type": "Link",
                "href": BASE_URL + settings.MEDIA_URL + "Leviathan%20Wakes/Drive/String%20Quartet.aac",
                "mediaType": "audio/aac"
            }
        },
    ],
}

expected_get_artist_1_response = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": BASE_URL + "/artists/1/",
    "type": "Group",
    "name": "Leviathan Wakes",
    "attributedTo": [
        {
            "type": "Person",
            "id": BASE_URL + "/users/1/",
            "name": "Amos Burton",
        },
        {
            "type": "Person",
            "id": BASE_URL + "/users/2/",
            "name": "James Holden",
        },
        {
            "type": "Person",
            "id": BASE_URL + "/users/3/",
            "name": "Naomi Nagata",
        },
        {
            "type": "Person",
            "id": BASE_URL + "/users/4/",
            "name": "Bobbie Draper",
        },
        {
            "type": "Person",
            "id": BASE_URL + "/users/5/",
            "name": "Shed Garvey",
        },
        {
            "type": "Person",
            "id": BASE_URL + "/users/6/",
            "name": "Clarissa Mao",
        },
    ],
}

expected_get_track_1_response = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": BASE_URL + "/tracks/1/",
    "type": "Audio",
    "name": "String Quartet No. 6",
    "url": {
        "type": "Link",
        "href": BASE_URL + settings.MEDIA_URL + "Leviathan%20Wakes/The%20Last%20Flight%20of%20the%20Cassandra/String%20Quartet%20No.%206/LudwigVanBeetho_GViOF3Q.6.flac",
        "mediaType": "audio/aac"
    }
}