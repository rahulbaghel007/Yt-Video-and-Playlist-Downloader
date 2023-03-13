from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLxUy0jIjSSKaaeNpsu3LmK3iAL2ct8o3L")
 
print(f'Downloading :{playlist.title}')

for video in playlist.videos:
    video.streams.first().download()
    # print("Done" )
print("Successfully")