# vk_music [![Build Status](https://travis-ci.org/stleon/vk_music.svg?branch=master)](https://travis-ci.org/stleon/vk_music)

Very-very simple vk music downloader.

Its a first version, if you need more functionality - create an **Issue**.

If you like it - **star** and share.

## Client id

You need **CLIENT_ID**. Create app [here](https://vk.com/dev/standalone).

## Token

Get token:

```
https://oauth.vk.com/authorize?client_id=CLIENT_ID&scope=audio,offline&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token
```

And save it to **Environment variable** `TOKEN`.

```
export TOKEN=very_security_token
```

## Required

- **Python 3.5**
- **[requests](https://github.com/kennethreitz/requests)**
- **[pytest](https://github.com/pytest-dev/pytest)**

```
pip install -r requirements.txt
```

## How to start

```
python3.5 vk_music.py
```

Or you can run simple

```
$ ipython --no-banner
In [1]: import os

In [2]: from vk_music import VkMusic

In [3]: VK_ID = 1  # your vk id

In [4]: vk = VkMusic(vk_id=VK_ID, token=os.getenv('TOKEN'))

In [5]: for track in vk.tracks():
   ...:     vk.track_save(track)
   ...:
```

## Tests

You can run tests by this command:

```
py.test -v --durations=10 --ignore=env
```