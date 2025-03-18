import json

from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from master_collection.tests import oracle
BASE_URL = settings.HOST

def build_activitypub_album(album):
    return NotImplemented

# Create your tests here.
class DereferencingViewsTest(TestCase): 
    fixtures = ["users", "artists", "albums", "tracks"]
    maxDiff = None

# Dereferencer tests
## Fully Populated
    def test_get_fully_populated_album(self):
        response = self.client.get(reverse("album", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(oracle.get_fully_populated_album))
        
    def test_get_fully_populated_artist(self):
        response = self.client.get(reverse("artist", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(oracle.get_fully_populated_artist))

    def test_get_fully_populated_track(self):
        response = self.client.get(reverse("track", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(oracle.get_fully_populated_track))
## Minimally Populated
    def test_get_minimally_populated_album(self):
        response = self.client.get(reverse("album", args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(oracle.get_minimally_populated_album))
        
    def test_get_minimally_populated_artist(self):
        response = self.client.get(reverse("artist", args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(oracle.get_minimally_populated_artist))

    def test_get_minimally_populated_track(self):
        response = self.client.get(reverse("track", args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, json.dumps(oracle.get_minimally_populated_track))