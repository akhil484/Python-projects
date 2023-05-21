from pytube import YouTube
import os

url = "https://www.youtube.com/watch?v=ESwa1JTONd8&list=PLL03-AvDshL_nodH_z3iTAQZi2pP6gl-0"
    
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()
out_file = video.download()

new_file = 'audio.mp3'
os.rename(out_file, new_file)