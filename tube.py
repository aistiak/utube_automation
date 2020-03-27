from pytube import YouTube
import string
import sys 
import os 

link = "https://www.youtube.com/watch?v=9hIgYEF42so&list=RD9hIgYEF42so&start_radio=1"
local_path = "store"
yt = YouTube(link)
# extract name remove everything except alphabet and replace with underscore 
print('extracting name')
name = ''.join(list(map(lambda v : v if v in string.ascii_letters else '_',yt.title)))
# low quality audio + video 
print('downloading audio => ' + name )
yt.streams.filter(file_extension="mp4",progressive=True).order_by('resolution')[-1].download(filename="audio")
# HQ video 
print('downloading video => ' + name )
yt.streams.order_by('resolution')[-1].download(filename="video")
# merge the audio and video 
print('merging audio & video audio of => ' + name )
os.system("ffmpeg.exe -loglevel warning -i video.webm -i audio.mp4 -c copy {}/{}.mkv -y".format(local_path,name))
# remove temporary files 
print('removing temporary files')
os.system("del video.webm audio.mp4")
