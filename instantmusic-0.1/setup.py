from setuptools import setup
from sys import platform

setup(name='instantmusic',
      version='1.2',
      description='Instantly download any song! Without knowing the name of the song!!!!',
      url='https://github.com/yask123/Instant-Music-Downloader',
      author='Yask Srivastava',
      author_email='yask123@gmail.com',
      license='MIT',
      packages=['instantmusic'],
      scripts=['bin/instantmusic'],
      install_requires=[
          'youtube-dl',
          'BeautifulSoup4',
          'eyed3',
          'requests'
      ] + (['pyreadline'] if platform.startswith('win') else []),
      zip_safe=False)
