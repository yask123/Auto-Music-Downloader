#!/usr/bin/env python
"""setup file."""
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
    name='Instant Music Downloader',
    version='1.0',
    description='Downloads Music From The Web',
    long_description=read_md('README.md'),
    author='yask123',
    author_email='yask123@gmail.com',
    url='https://github.com/yask123/Instant-Music-Downloader',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
