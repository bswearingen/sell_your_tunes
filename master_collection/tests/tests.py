import json

from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .utils import create_albums, create_artists, create_users, create_tracks
from .utils import expected_get_albums_response, expected_get_artists_response
BASE_URL = settings.HOST

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

        for album in cls.albums:
            create_tracks(album, ["First Track", "Second Track", "Third Track"])
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
        response = self.client.get(reverse("albums"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_albums_response))

    # def test_get_artists(self):
    #     response = self.client.get(reverse("artists"))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertJSONEqual(response.content, json.dumps(expected_get_artists_response))

    def test_get_album(self):
        response = self.client.get(reverse("album", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_artists_response))
        
    def test_get_artist(self):
        response = self.client.get(reverse("artist", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_artists_response))

    def test_get_track(self):
        response = self.client.get(reverse("track", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_artists_response))