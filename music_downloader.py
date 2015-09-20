# /usr/local/bin/python

import os
import glob
from bs4 import BeautifulSoup
import urllib2
from urllib import quote_plus as qp

# High Quality Songs, yeah baby!
DEFAULT_AUDIO_QUALITY = '320K'

search = ''
# We do not want to accept empty inputs :)
while search == '':
  search = raw_input('Enter songname/ lyrics/ artist.. or whatever \n>')
search = qp(search)

print('Making a Query Request! ')

# Magic happens here.
response = urllib2.urlopen('https://www.youtube.com/results?search_query='+search)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
    	# May change when Youtube is updated in the future.
    	video_link = link.get('href')
    	break
title = soup.find("a", "yt-uix-tile-link").text
print(title)

# Links are relative on page, making them absolute.
video_link =  'http://www.youtube.com/'+video_link
command = ('youtube-dl --extract-audio --audio-format mp3 --audio-quality ' +
           DEFAULT_AUDIO_QUALITY + ' ' +video_link)

# Youtube-dl is a proof that god exists.
print ('Downloading...')
os.system(command)
