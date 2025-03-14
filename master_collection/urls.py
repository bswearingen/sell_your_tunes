from django.urls import path

from . import views

urlpatterns = [
    # Dereferencers
    # ex: /collection/albums/5/
    path("albums/<int:album_id>/", views.get_album, name="album"),
    # ex: /collection/artists/5/
    path("artists/<int:artist_id>/", views.get_artist, name="artist"),
    # ex: /collection/tracks/5/
    path("tracks/<int:track_id>/", views.get_track, name="track"),
]