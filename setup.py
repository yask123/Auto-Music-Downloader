#!/usr/bin/env python
"""setup file."""
from sys import platform
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')  # NOQA
except ImportError:
    print(
        "warning: pypandoc module not "
        "found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()  # NOQA

setup(
    name='instantmusic',
    version='1.2',
    description='Instantly download any song! Without knowing the name of the song!!!!',
    long_description=read_md('README.md'),
    author='Yask Srivastava',
    author_email='yask123@gmail.com',
    url='https://github.com/yask123/Instant-Music-Downloader',
    license='MIT',
    packages=['instantmusic'],
    scripts=['bin/instantmusic'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'youtube-dl',
        'BeautifulSoup4',
        'eyed3',
        'requests'
    ] + (['pyreadline'] if platform.startswith('win') else []),
    zip_safe=False,
)
