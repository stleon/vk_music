from vk_music import Track


class TestTrack:
    def setup_class(self):
        self.track = Track(artist=' Test Artist ', title=' Test /title/ ',
                           url='http://domain.com/21731082371?test')

    def test_get_artist(self):
        assert self.track.get_artist == 'Test Artist'

    def test_get_title(self):
        assert self.track.get_title == 'Test title'

    def test_get_download_url(self):
        assert self.track.download_url == 'http://domain.com/21731082371'

    def test_str(self):
        assert str(self.track) == 'Test Artist - Test title.mp3'
