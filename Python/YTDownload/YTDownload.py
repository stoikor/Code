from pytube import YouTube
from sys import argv

link = argv[1]
res = argv[2]
yt = YouTube(link)

print(yt.title)

yd = yt.streams.get_by_resolution(res)
yd.download("G:/Test/YTD")