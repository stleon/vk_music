class Track():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def get_artist(self):
        return self.artist.strip()

    @property
    def get_title(self):
        return self.title.strip().replace('/', '')

    @property
    def download_url(self):
        return self.url.split("?")[0]

    def __str__(self):
        return '%s - %s.mp3' % (self.get_artist, self.get_title)
