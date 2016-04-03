import os

import pytest


def check_config(env_var):
    __tracebackhide__ = True
    if not os.getenv(env_var):
        pytest.fail("not configured environment variable: %s" % env_var)


def test_token():
    check_config('TOKEN')


def test_vk_id():
    check_config('VK_ID')
