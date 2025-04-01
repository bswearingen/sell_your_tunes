from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Album, Artist, Track

from django.conf import settings

# Dereferencers for ActivityPub
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

# How will users interact with the masters collection?
# They'll only have access to their own items
# List view, detail view, CRUD view,

class AlbumsView(LoginRequiredMixin, generic.ListView):
    template_name = "master_collection/index.html"
    login_url = "/accounts/login/"
    next_page = "/albums/"

    def get_queryset(self):
        # TODO: Limit this to albums that the user is in the release band for
        return Album.objects.all()

def get_my_albums(request):
    # Ensure user is logged in
    # If not redirect to login flow
    # ListView of albums
    return NotImplementedError

class AlbumCreate(PermissionRequiredMixin, CreateView):
    model = Album
    fields = '__all__'
    permission_required = 'master_collection.add_album'