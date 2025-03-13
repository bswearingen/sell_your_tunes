from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Our two roots for exploring the collection 
    # ex: /collection/albums/
    path("albums/", views.get_albums, name="albums"),
    # ex: /collection/artists/
    path("artists/", views.get_artists, name="artists"),

    # Dereferencers
    # ex: /collection/albums/5/
    path("albums/<int:album_id>/", views.get_album, name="album"),
    # ex: /collection/artists/5/
    path("artists/<int:artist_id>/", views.get_artist, name="artist"),
    # ex: /collection/recordings/5/
    path("recordings/<int:recording_id>/", views.get_recording, name="recording"),
    # ex: /collection/tracks/5/
    path("tracks/<int:track_id>/", views.get_track, name="track"),
]