import os
from types import GeneratorType

import pytest

from vk_music import VkMusic


@pytest.yield_fixture()
def vk_api(tmpdir):
    yield VkMusic(vk_id=os.getenv('VK_ID'), token=os.getenv('TOKEN'),
                  path=str(tmpdir))


@pytest.yield_fixture()
def first_track(vk_api):
    yield vk_api.tracks().__next__()


@pytest.yield_fixture()
def track_save(vk_api, first_track):
    yield vk_api.track_save(first_track)


def test_path(vk_api):
    assert os.path.exists(vk_api.path)


@pytest.mark.skipif(os.getenv('TRAVIS') != None, reason="Validation required")
def test_api_request(vk_api):
    r = vk_api.api_request(method_name='audio.get',
                           owner_id=vk_api.vk_id)
    assert isinstance(r, dict)


@pytest.mark.skipif(os.getenv('TRAVIS') != None, reason="Validation required")
def test_tracks(vk_api):
    assert isinstance(vk_api.tracks(), GeneratorType)


@pytest.mark.skipif(os.getenv('TRAVIS') != None, reason="Validation required")
def test_track_save_not_exists(vk_api, first_track):
    vk_api.track_save(first_track)
    assert str(first_track) in os.listdir(vk_api.path)


@pytest.mark.skipif(os.getenv('TRAVIS') != None, reason="Validation required")
def test_track_save_not_exists_bool(track_save):
    assert track_save == True


@pytest.mark.skipif(os.getenv('TRAVIS') != None, reason="Validation required")
def test_track_save_exists(vk_api, first_track, track_save):
    exists = vk_api.track_save(first_track)
    assert exists == False
