import json

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

from .models import Artist, Album, Track, Recording

BASE_URL = settings.HOST

def create_users(usernames):
    users = []
    for username in usernames:
        users.append(User.objects.create_user(username=username, password='12345'))

    return users

def create_artists(artist_names, users):
    artists = []
    for artist_name in artist_names:
        artist = Artist.objects.create(name=artist_name)
        artist.members.set([users.pop(0), users.pop(0)])
        artists.append(artist)

    return artists

def create_albums(artist, album_names):
    albums = []
    for album_name in album_names:
        album = Album.objects.create(
            name=album_name,
            release_date="1990-01-01",
            release_artist=artist,
        )
        albums.append(album)
    
    return albums

def build_activitypub_album(album):
    return NotImplemented

# Create your tests here.
class DereferencingViewsTest(TestCase): 
    maxDiff = None
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.users = create_users([
            "NoAlbum1",
            "NoAlbum2",
            "OneTime1",
            "OneTime2",
            "Multipack1",
            "Multipack2",
        ])

        cls.artists = create_artists([
            "No Album",
            "One Time",
            "Multipack",
        ], cls.users)

        cls.albums = create_albums(cls.artists[1], ["1st Album"])
        cls.albums += create_albums(cls.artists[2], ["2nd Album", "3rd Album","4th Album","5th Album",])
    
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        for user in cls.users:
            user.delete()
        for artist in cls.artists:
            artist.delete()
        for album in cls.albums:
            album.delete()

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the master_collection index.")


    def test_get_albums(self):
        expected = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "sell_your_tune's master album collection",
            "type": "OrderedCollection",
            "totalItems": 5,
            "orderedItems": [
                {
                    "type": "Audio",
                    "name": "1st Album",
                    "id": BASE_URL + "albums/1/",
                    "release_date": "1990-01-01",
                    "release_artist": BASE_URL + "artists/2/",
                },
                {
                    "type": "Audio",
                    "name": "2nd Album",
                    "id": BASE_URL + "albums/2/",
                    "release_date": "1990-01-01",
                    "release_artist": BASE_URL + "artists/3/",
                },
                {
                    "type": "Audio",
                    "name": "3rd Album",
                    "id": BASE_URL + "albums/3/",
                    "release_date": "1990-01-01",
                    "release_artist": BASE_URL + "artists/3/",
                },
                {
                    "type": "Audio",
                    "name": "4th Album",
                    "id": BASE_URL + "albums/4/",
                    "release_date": "1990-01-01",
                    "release_artist": BASE_URL + "artists/3/",
                },
                {
                    "type": "Audio",
                    "name": "5th Album",
                    "id": BASE_URL + "albums/5/",
                    "release_date": "1990-01-01",
                    "release_artist": BASE_URL + "artists/3/",
                },
            ]
        } 
        response = self.client.get(reverse("albums"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected))
