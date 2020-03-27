pytube library was user to download video 
since HQ webm file has no audio so we downloaded two files one .mp4 LQ vid with sound and one .webm file  with hQ video and then we merge those two files with 
"ffmpeg" which is a c librarby(binary) 
the command was `ffmpeg -i vid.webm -i aud.mp4 -c copy output.mkv`


links :
https://github.com/nficano/pytube

https://stackoverflow.com/questions/47649536/python-download-youtube-with-specific-filename

https://stackoverflow.com/questions/35939131/how-can-i-merge-webm-audio-file-and-a-mp4-video-file-using-java/35939357

https://superuser.com/questions/277642/how-to-merge-audio-and-video-file-in-ffmpeg