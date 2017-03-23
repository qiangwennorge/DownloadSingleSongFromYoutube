# -*- coding: utf-8 -*-
# encoding=utf8 

"""
Created on Sun Mar  5 17:15:14 2017

@author: qiangwennorge
"""
from __future__ import unicode_literals
import youtube_dl
from bs4 import BeautifulSoup
import urllib2
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

# Fetch the HTML file where the videos are listed
StartingUrl = 'https://www.youtube.com/playlist?list=PLXgUykwqp2GSmCNJjpjmbw9YWNeBx-9rr'
StartingResponse = urllib2.urlopen(StartingUrl)
StartingHtml = StartingResponse.read()

# Make a soup --- parse the HTML file
StartingSoup = BeautifulSoup(StartingHtml,"html.parser")

# Find the video location
SingleSongUrlTagList = StartingSoup.find_all('td','pl-video-title')

SingleSongName = StartingSoup.find_all('td','pl-video-title')[0].a.get_text().strip()

# Download each video
for SingleSongUrlTag in SingleSongUrlTagList:
    SingleSongUrl = SingleSongUrlTag.a.get('href')
    SingleSongName = SingleSongUrlTag.a.get_text().strip()
    print SingleSongName
    try:
        SingleSongUrl = "http://www.youtube.com" + SingleSongUrl
        ydl_opts = {}
        '''
        class MyLogger(object):
            def debug(self, msg):
                pass

            def warning(self, msg):
                pass

            def error(self, msg):
                print(msg)


        def my_hook(d):
            if d['status'] == 'finished':
                print('Done downloading, now converting ...')
           
        ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',}],
                    'logger': MyLogger(),
                    'progress_hooks': [my_hook],
                    'outtmpl': SingleSongName + '.mp3'
        }'''
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([SingleSongUrl])
    except Exception:
        pass

