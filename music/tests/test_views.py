from django.test import TestCase, Client

from music.models import Artist


class TestArtistViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Test Artist")
        self.client = Client()

    def test_get_all_albums(self):
        response = self.client.get('/artists/')
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]['name'], 'Test Artist')