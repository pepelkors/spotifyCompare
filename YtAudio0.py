#from re import search
from turtle import reset
from pytube import YouTube
import os
from apiclient.discovery import build

with open('key.txt') as f:
    dev = f.readlines()

youtube = build('youtube', 'v3',developerKey = dev)

def download_video(song_name, downPath):
    print("started")
    if song_name == '':
        print("No song name entered")
        return
    
    request = youtube.search().list(q=song_name, part='snippet', type='video', maxResults = 1)
    res = request.execute()
    videoid = res['items'][0]['id']['videoId']
    name = res['items'][0]['snippet']['title']
    channelName = res['items'][0]['snippet']['channelTitle']
    name = name + channelName
    print(name)
    yt = YouTube("https://www.youtube.com/watch?v=" + videoid)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=downPath)
    base, ext = os.path.splitext(out_file)
    new_file = name + ".mp3"
    os.rename(out_file, new_file)
    print("done")