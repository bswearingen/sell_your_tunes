from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import json

from .models import Album, Artist, Track

from django.conf import settings

def get_album(request, album_id): 
    album = get_object_or_404(Album, pk=album_id)
    result = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": '/'.join([settings.HOST, "albums", str(album_id), '']),
        "type": "OrderedCollection",
        "name": album.name,
        "summary": album.name + " by " + album.release_artist.name,
        "totalItems": album.track_set.count()
    }

    contributing_artists = [{
        "id": '/'.join([settings.HOST, "artists", str(album.release_artist.pk), '']),
        "type": "Group",
        "name": album.release_artist.name,
    }]
    for artist in album.contributing_artists.all():
        contributing_artists.append({
            "id": '/'.join([settings.HOST, "artists", str(artist.pk), '']),
            "type": "Group",
            "name": artist.name,
        })
    result["attributedTo"] = contributing_artists

    tracks = []
    for track in album.track_set.all():
        if track.streamable_recording:
            tracks.append({
                "id": '/'.join([settings.HOST, "tracks", str(track.pk), '']),
                "type": "Audio",
                "name": track.name,
                "url": {
                    "type": "Link",
                    "href": settings.HOST + track.streamable_recording.url,
                    "mediaType": "audio/aac"
                }
            })
    result["orderedItems"] = tracks
    return JsonResponse(result)


def get_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    result = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id":  '/'.join([settings.HOST, "artists", str(artist_id), '']),
        "type": "Group",
        "name": artist.name,
    }
    attributed_to = []
    for member in artist.members.all():
        attributed_to.append(
            {
                "type": "Person",
                "id": '/'.join([settings.HOST, "users", str(member.pk), '']),
                "name": member.username,
            }
        )
    result["attributedTo"] = attributed_to

    return JsonResponse(result)

def get_track(request, track_id): 
    track = get_object_or_404(Track, pk=track_id)
    result = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": '/'.join([settings.HOST, "tracks", str(track_id), '']),
        "type": "Audio",
        "name": track.name,
    }
    if track.streamable_recording:
        result["url"] = {
            "type": "Link",
            "href": settings.HOST + track.streamable_recording.url,
            "mediaType": "audio/aac"
        }
    return JsonResponse(result)