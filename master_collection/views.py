from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import json

from .models import Album, Artist, Track

from django.conf import settings

def get_album(request, album_id): 
    album = get_object_or_404(Album, pk=album_id)
    return JsonResponse(album.activitypub())


def get_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return JsonResponse(artist.activitypub())

def get_track(request, track_id): 
    track = get_object_or_404(Track, pk=track_id)
    track.activitypub()
    return JsonResponse(track.activitypub())