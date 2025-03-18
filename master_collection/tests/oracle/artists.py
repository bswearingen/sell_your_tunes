from django.conf import settings

get_fully_populated_artist = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": settings.HOST + "/artists/1/",
    "type": "Group",
    "name": "Leviathan Wakes",
    "summary": "Ice-hauling detectives",
    "icon": {
        "type": "Image",
        "altText": "A picture of Leviathan Wakes",
        "url": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/images/icon.jpg",
    },
    "image": {
        "type": "Image",
        "altText": "A banner picture of Leviathan Wakes",
        "url": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/images/banner.jpg",
    },
    "location": {
        "name": "Montréal",
        "type": "Place"
    },
    "attributedTo": [
        {
            "type": "Person",
            "id": settings.HOST + "/users/1/",
            "name": "Amos Burton",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/2/",
            "name": "James Holden",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/3/",
            "name": "Naomi Nagata",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/4/",
            "name": "Bobbie Draper",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/5/",
            "name": "Shed Garvey",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/6/",
            "name": "Clarissa Mao",
        },
    ],
}

get_minimally_populated_artist = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": settings.HOST + "/artists/2/",
    "type": "Group",
    "name": "Leviathan Falls",
    "attributedTo": [
        {
            "type": "Person",
            "id": settings.HOST + "/users/1/",
            "name": "Amos Burton",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/5/",
            "name": "Shed Garvey",
        },
        {
            "type": "Person",
            "id": settings.HOST + "/users/6/",
            "name": "Clarissa Mao",
        },
    ],
}