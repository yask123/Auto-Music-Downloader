#!/usr/bin/env python

import os
import sys
import glob
from bs4 import BeautifulSoup
import urllib2
from urllib import quote_plus as qp

# High Quality Songs, yeah baby!
DEFAULT_AUDIO_QUALITY = '320K'

search = raw_input('Enter songname/ lyrics/ artist.. or whatever\n> ')
# Exit if input is empty
if search == '':
    sys.exit()

print('Making a Query Request! ')

# Magic happens here.
search = qp(search)
response = urllib2.urlopen('https://www.youtube.com/results?search_query=' + search)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    if '/watch?v=' in link.get('href'):
        # May change when Youtube Website may get updated in the future.
        video_link = link.get('href')
        break
    
# Print video title and prompt for download
title = soup.find("a", "yt-uix-title-link").text
print("Found: " + title)
prompt = raw_input("Download song (y/n)? ")
if prompt != "y":
    sys.exit()
    
# Links are relative on page, making them absolute.
video_link =  'http://www.youtube.com/'+video_link
command = ('youtube-dl --extract-audio --audio-format mp3 --audio-quality ' +
           DEFAULT_AUDIO_QUALITY + ' ' + video_link)

# Youtube-dl is a proof that god exists.
print ('Downloading...')
os.system(command)

