from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .models import Album

# Endpoints for usecase
# Get collection of albums (get_albums)
# Dereference album (get_album)
# Derefernece track (get_track)

# Get collection of artists (get_artists)
# Dereference artist (get_artist)
# Dereference album [see above.]

BASE_URL = "https://www.sell_your_tunes.com/"
def index(request):
    return HttpResponse("Hello, world. You're at the master_collection index.")

def get_albums(request): 
    # TODO: Pagination
    ordered_collection = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "summary": "sell_your_tune's master album collection",
        "type": "OrderedCollection",
        "totalItems": Album.objects.count()
    }
    ordered_items = []
    for album in Album.objects.all():
        ordered_items.append(
            {
                "type": "Audio",
                "name": album.name,
                "id": BASE_URL + "albums/" + str(album.pk) + "/",
                "release_date": str(album.release_date),
                "release_artist": BASE_URL + "artists/" + str(album.release_artist.pk) + "/"
            }
        )

    ordered_collection["orderedItems"] = ordered_items
    return JsonResponse(ordered_collection)

def get_artists(request):
    return HttpResponse("Hello, world. You're at the artists index.")

def get_album(request, album_id): 
    return HttpResponse("Hello, world. You're at the get_album endpoint. You queried: " + str(album_id))
def get_artist(request, artist_id):
    return HttpResponse("Hello, world. You're at the get_artist endpoint. You queried: " + str(artist_id))
def get_track(request, track_id): 
    return HttpResponse("Hello, world. You're at the get_track endpoint.. You queried: " + str(track_id))