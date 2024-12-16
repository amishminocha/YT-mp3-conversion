from pytube import YouTube, Playlist
import os 

url = input("Enter url link of playlist: ")
playlist = Playlist(url)
list_of_videos = playlist.videos

for video in list_of_videos:
    print('Downloading \'' + video.title + '\'...')
    downloaded_audio = video.streams.filter(only_audio=True).first().download()
    filename = os.path.splitext(downloaded_audio)
    os.rename(downloaded_audio, filename[0]+'.mp3')
    print('Downloaded!!!')

print('Playlist downloaded! Done!!!')
