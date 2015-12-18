# Instantly download any song! :guitar: :notes: :musical_score: :trumpet: :violin:
[![Build Status](https://travis-ci.org/yask123/Instant-Music-Downloader.svg?branch=master)](https://travis-ci.org/yask123/Instant-Music-Downloader)
[![PyPI](https://img.shields.io/pypi/v/Instantmusic.svg)](https://pypi.python.org/pypi/instantmusic/1.3)
[![PyPI](https://img.shields.io/pypi/dw/Instantmusic.svg)](https://pypi.python.org/pypi/instantmusic/1.3)

Without knowing its name!!!!

> This is so cool!

## Installation by [Pip](http://pip.readthedocs.org/en/stable/installing/)
For Python 2.7

```bash
$ sudo pip install instantmusic
```

For Python 3.4

```bash
$ sudo pip3 install instantmusic
```

### Note:
You would also need `libav` to download in `.mp3` format.

#### On Mac Os X
##### Installation by [Brew](https://brew.sh)
```bash
 $ brew install libav
 ```
 
#### On Ubuntu 

```bash
 $ sudo apt-get install libav-tools 
```
#### On Windows
>[See this](https://github.com/yask123/Instant-Music-Downloader/issues/19) 

## Usage

```bash
$ instantmusic 
```

```zsh
>> Enter songname/ lyrics/ artist.. or whatever

i tried so hard and got so far 

>>Downloaded Linkin Park - In The End
```

```zsh
>> Enter songname/ lyrics/ artist.. or whatever

another turning point a fork stuck in the road

>>Downloaded Green Day - Good Riddance
```

```zsh
>> Enter songname/ lyrics/ artist.. or whatever

yeh hosla kaise jhuke

>>Downloaded Yeh Hausla Kaise Jhuke - Salim-Sulaiman
```
### Options

```
❯ instantmusic -h                                                   
usage: instantmusic [-h] [-p] [-q] [-s SONG [SONG ...]]
                    [-l SONGLIST [SONGLIST ...]] [-f FILE [FILE ...]]

Instantly download any song!

optional arguments:
  -h, --help            show this help message and exit
  -p                    Turn off download prompts
  -q                    Run in quiet mode. Automatically turns off prompts.
  -s SONG [SONG ...]    Download a single song.
  -l SONGLIST [SONGLIST ...]
                        Download a list of songs, with lyrics separated by a
                        comma (e.g. "i tried so hard and got so far, blackbird
                        singing in the dead of night, hey shawty it's your
                        birthday).
  -f FILE [FILE ...]    Download a list of songs from a file input. Each line
                        in the file is considered one song.
```

### MP3 Tags
> WIP


The script automatically embeds `id3` tags to the downloaded `.mp3` file.

It will grab following meta data:

1. Track title (From YT)
2. Artist (From YT)
3. Album name (From metrolyrics.com)
4. Album art (From google images)
5. Lyrics  (From metrolyrics.com) 

<img src="http://i.imgur.com/fNXww62.png" height="50%" width="50%">


```bash
$ sudo pip install fixalbumart

❯cd MyMusic

❯fixalbumart

>> Fixing taylor swift - love story
>> In the end - Linkin park 
......

>> Fixed all songs

```



### Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=H2GQc81hpBE
" target="_blank"><img src="http://img.youtube.com/vi/H2GQc81hpBE/0.jpg" 
alt="Demo" width="240" height="180" border="10" /></a>


## Requirements
1. Youtube-dl
2. BeautifulSoup

## Disclaimer

Downloading copyrighted material may be illegal in your country. Use at your own risk.


## The MIT License
> Copyright (c) 2015 Yask Srivastava http://iyask.me

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
