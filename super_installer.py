#!/usr/bin/env python
import os
os.system('pip install -r requirements.txt')
current_path = os.getcwd()

os.system('cd ~')
prof_path = os.getenv("HOME")
os.system('mkdir ~/.music_downloader')
os.system('cp '+current_path+'/music_downloader.py ~/.music_downloader')

with open(prof_path+'/.profile', 'a') as f:
    f.write('PATH="$PATH:~/.music_downloader"')
