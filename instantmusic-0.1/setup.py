from setuptools import setup

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
          'eyed3'
      ],
      zip_safe=False)
