#usr/local/bin/python

import os
import glob
from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

# This is the python 3 version of music_downloader.py

# High Quality Songs setting
DEFAULT_AUDIO_QUALITY = '320K'

search = ''
# dont accept empty strings
while search == '':
  search = input('Enter the song name, lyrics, or artist: ')
search = parse.quote_plus(search)

print('Searching.....')

# search youtube
response = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
        print(link.get('href'))
        # this may change if/when youtube updates in the future.
        video_link = link.get('href')
        break

# make relative youtube links absolute links
video_link = 'http://www.youtube.com/'+video_link
command = ('youtube-dl --extract-audio --audio-format mp3 --audio-quality ' +
           DEFAULT_AUDIO_QUALITY + ' ' +video_link)

#show that we are downloading and issue youtube-dl command to system
print('Downloading...')
os.system(command)
