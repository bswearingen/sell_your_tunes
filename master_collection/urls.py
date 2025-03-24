from django.urls import path

from . import views

app_name = "master_collection"
urlpatterns = [
    # User views
    path("albums/", views.IndexView.as_view(), name="index"),
    # Dereferencers
    # ex: /collection/albums/5/
    path("albums/<int:album_id>/", views.get_album, name="album"),
    # ex: /collection/artists/5/
    path("artists/<int:artist_id>/", views.get_artist, name="artist"),
    # ex: /collection/tracks/5/
    path("tracks/<int:track_id>/", views.get_track, name="track"),
]