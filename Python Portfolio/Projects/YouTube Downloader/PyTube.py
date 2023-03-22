from pytube import YouTube

yt = YouTube("https://youtu.be/YnNchZ_2yxQ")

print("Title:", yt.title)

print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('YouTubedownloads')
