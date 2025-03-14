from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from .models import Album, Artist

from django.conf import settings

# Endpoints for usecase
# Get collection of albums (get_albums)
# Dereference album (get_album)
# Derefernece track (get_track)

# Get collection of artists (get_artists)
# Dereference artist (get_artist)
# Dereference album [see above.]

BASE_URL = settings.HOST

def get_album(request, album_id): 
    return HttpResponse("Hello, world. You're at the get_album endpoint. You queried: " + str(album_id))
def get_artist(request, artist_id):
    return HttpResponse("Hello, world. You're at the get_artist endpoint. You queried: " + str(artist_id))
def get_track(request, track_id): 
    return HttpResponse("Hello, world. You're at the get_track endpoint.. You queried: " + str(track_id))