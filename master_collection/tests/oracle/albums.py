from django.conf import settings

get_fully_populated_album = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": settings.HOST + "/albums/1/",
    "type": "OrderedCollection",
    "name": "Drive",
    "published": "2012-11-27",
    "summary": "Drive by Leviathan Wakes",
    "icon": {
        "type": "Image",
        "altText": "A picture of Drive",
        "url": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/Drive/images/cover.jpg",
    },
    "image": {
        "type": "Image",
        "altText": "A spine picture of Drive",
        "url": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/Drive/images/spine.jpg",
    },
    "attributedTo": [
        {
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
        },
        {
            "id": settings.HOST + "/artists/5/",
            "type": "Group",
            "name": "Babylon's Ashes",
            "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "icon": {
                "type": "Image",
                "altText": "A picture of Babylon's Ashes",
                "url": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/images/icon.jpg",
            },
            "image": {
                "type": "Image",
                "altText": "A banner picture of Babylon's Ashes",
                "url": settings.HOST + settings.MEDIA_URL + "Babylon\'s%20Ashes/images/banner.jpg",
            },
            "location": {
                "name": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec,.",
                "type": "Place"
            },
        },
    ],
    "totalItems": 1,
    "orderedItems": [
        {
            "id": settings.HOST + "/tracks/3/",
            "type": "Audio",
            "name": "Symphony No. 1",
            "url": {
                "type": "Link",
                "href": settings.HOST + settings.MEDIA_URL + "Leviathan%20Wakes/Drive/Symphony%20No.%201.aac",
                "mediaType": "audio/aac"
            }
        },
    ],
}

get_minimally_populated_album = {
    "@context": "https://www.w3.org/ns/activitystreams",
    "id": settings.HOST + "/albums/2/",
    "type": "OrderedCollection",
    "name": "The Churn",
    "published": "2014-04-29",
    "attributedTo": [
        {
            "id": settings.HOST + "/artists/6/",
            "type": "Group",
            "name": "Caliban's War",
        },
        {
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
        },
        {
            "id": settings.HOST + "/artists/3/",
            "type": "Group",
            "name": "Babylon's Ashes",
            "summary": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "icon": {
                "type": "Image",
                "altText": "A picture of Babylon's Ashes",
                "url": settings.HOST + settings.MEDIA_URL + "Persepolis%Rising/images/icon.jpg",
            },
            "image": {
                "type": "Image",
                "altText": "A banner picture of Babylon's Ashes",
                "url": settings.HOST + settings.MEDIA_URL + "Persepolis%Rising/images/banner.jpg",
            },
            "location": {
                "name": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec,.",
                "type": "Place"
            },
        },
    ],
    "totalItems": 2,
    "orderedItems": [
        {
            "id": settings.HOST + "/tracks/7/",
            "type": "Audio",
            "name": "Symphony No. 1",
            "url": {
                "type": "Link",
                "href": settings.HOST + settings.MEDIA_URL + "Caliban's War/The Churn/Russian Easter Festival.aac",
                "mediaType": "audio/aac"
            }
        },
        {
            "id": settings.HOST + "/tracks/9/",
            "type": "Audio",
            "name": "Marriage of Figaro",
            "url": {
                "type": "Link",
                "href": settings.HOST + settings.MEDIA_URL + "Caliban's War/The Churn/Marriage of Figaro.aac",
                "mediaType": "audio/aac"
            }
        },
    ],
}