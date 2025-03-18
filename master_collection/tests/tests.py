import json

from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .utils import expected_get_album_1_response, expected_get_artist_1_response, expected_get_track_1_response
BASE_URL = settings.HOST

def build_activitypub_album(album):
    return NotImplemented

# Create your tests here.
class DereferencingViewsTest(TestCase): 
    fixtures = ["users", "artists", "albums", "tracks"]
    maxDiff = None

# Happy path dereferencers
    def test_get_album(self):
        response = self.client.get(reverse("album", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_album_1_response))
        
    def test_get_artist(self):
        response = self.client.get(reverse("artist", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_artist_1_response))

    def test_get_track(self):
        response = self.client.get(reverse("track", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(expected_get_track_1_response))