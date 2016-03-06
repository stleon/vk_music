import logging
import os

import requests

# LOGGING

logging.basicConfig(format='%(levelname)s %(asctime)s %(name)s %(message)s',
                    datefmt='%H:%M:%S %d.%m.%y')
logger = logging.getLogger('app.' + __name__)
logger.setLevel(logging.INFO)


class VkMusic():
    def __init__(self, vk_id, token, path, api_v=5.45):
        self.vk_id, self.token = vk_id, token
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

    def audio_get(self):
        return self.api_request(method_name='audio.get',
                                owner_id=self.vk_id, )['response']['items']

    def audio_save(self, audio):
        file_name = '{path}/{artist} - {title}.mp3' \
            .format(path=self.path,
                    artist=audio['artist'].strip(),
                    title=audio['title'].strip().replace('/', ''))

        if not os.path.exists(file_name):
            with open(file_name, "wb") as f:
                logger.info('Saving: %s', file_name)
                r = requests.get(audio['url'].split("?")[0])
                f.write(r.content)

        else:
            logger.info('Exists: %s', file_name)


if __name__ == '__main__':

    vk_id_input = int(input('Enter VK ID: '))

    vk = VkMusic(vk_id=vk_id_input, token=os.getenv('TOKEN'),
                 path='audio')

    tracks = vk.audio_get()

    for track in tracks:
        vk.audio_save(track)
