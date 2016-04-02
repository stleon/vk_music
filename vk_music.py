import logging
import os

import requests

# LOGGING

logging.basicConfig(format='%(levelname)s %(asctime)s %(name)s %(message)s',
                    datefmt='%H:%M:%S %d.%m.%y')
logger = logging.getLogger('app.' + __name__)
logger.setLevel(logging.DEBUG)


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


class VkMusic():
    def __init__(self, vk_id, token, path='audio', api_v=5.45):
        self.vk_id, self.token = int(vk_id), token
        self.path, self.api_v = path, api_v
        self.base_url = "https://api.vk.com/method/" \
                        "{method_name}?{parametrs}" \
                        "&v={api_v}&access_token={token}"

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def api_request(self, method_name, **kwargs):
        parametrs = '&'.join(
            "{!s}={!r}".format(k, v) for (k, v) in kwargs.items())
        url = self.base_url.format(method_name=method_name, parametrs=parametrs,
                                   api_v=self.api_v,
                                   token=self.token)
        logger.info('Get request: %s', url)
        r = requests.get(url)
        return r.json()

    def tracks(self):
        r = self.api_request(method_name='audio.get',
                                     owner_id=self.vk_id, )
        logger.debug(r)
        track_lst = r['response']['items']
        return (Track(**data) for data in track_lst)

    def track_save(self, track):
        file_name = '{path}/{track}'.format(path=self.path, track=track)

        if not os.path.exists(file_name):
            with open(file_name, "wb") as f:
                logger.info('Saving: %s', file_name)
                r = requests.get(track.download_url)
                f.write(r.content)
            return True
        else:
            logger.info('Exists: %s', file_name)
            return False


if __name__ == '__main__':

    vk_id = input('Enter VK ID: ')

    vk = VkMusic(vk_id=vk_id if vk_id else os.getenv('VK_ID'),
                 token=os.getenv('TOKEN'))

    for track in vk.tracks():
        vk.track_save(track)
