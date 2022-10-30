from django.test import TestCase, Client

from music.models import Artist, Album

# from music.models import Artist
from music.serializers import ArtistSerializer, SongSerializer


class TestArtistSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Muhammadjon")
        self.artist1 = Artist.objects.create(name="Muhammadjon",picture='https://i.ytimg.com/vi/IG63eWOf5OM/maxresdefault.jpg')
    def test_data(self):
        data = ArtistSerializer(self.artist).data
        data1 = ArtistSerializer(self.artist1).data
        assert data['id'] is not None
        assert data1['picture'] is not None




# class TestSongSerializer(TestCase):
#     def setUp(self) -> None:
#         self.artist = Artist.objects.create(name="Test Artist")
#         self.album = Album.objects.create(artist=self.artist, title="Test Album")
#
#     def test_is_valid(self):
#         data = {
#             'title':'Test Song',
#             'album':self.album.id,
#             'cover': '',
#             'source': 'http://example.com/music.mp3',
#             'listened':0,
#         }
#         serializer = SongSerializer(data=data)
#
#         assert serializer['id'] is not None
#         print(serializer.errors)



