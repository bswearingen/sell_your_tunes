from django.conf import settings

get_fully_populated_track = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": settings.HOST + "/tracks/1/",
    "type": "Audio",
    "name": "String Quartet No. 6",
    "url": {
        "type": "Link",
        "href": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/The%20Last%20Flight%20of%20the%20Cassandra/String%20Quartet%20No.%206.aac",
        "mediaType": "audio/aac"
    },
}

get_minimally_populated_track = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": settings.HOST + "/tracks/2/",
    "type": "Audio",
    "name": "Goldberg Variations",
}