from setuptools import setup, find_packages

import vk_music

EMAIL = 'leonst998@gmail.com'

with open('README.md') as f1, open('requirements.txt') as f2:
    readme = f1.read()
    requirements = f2.read().splitlines()

setup(
    name=vk_music.__title__,
    version=vk_music.__version__,
    description='simple vkontakte music downloader',
    long_description=readme,
    author=vk_music.__author__,
    author_email=EMAIL,
    maintainer=vk_music.__author__,
    maintainer_email=EMAIL,
    url='https://github.com/stleon/vk_music',
    download_url='https://github.com/stleon/vk_music/archive/master.zip',
    packages=find_packages(),
    install_requires=requirements,
    license=vk_music.__license__,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',

    ),

)
